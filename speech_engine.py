import os
import re
import subprocess
import tempfile
import threading
import time
import warnings

DEFAULT_RATE = 150
MAX_CHUNK_LENGTH = 300
BACKENDS = ("pyttsx3", "powershell", "gtts")

_engine = None
_engine_lock = threading.RLock()
_disabled_backends = set()
_preferred_backend = None
_warning_shown = False


def _debug_enabled():
    return os.environ.get("SCP_TERMINAL_SPEECH_DEBUG") == "1"


def _configured_backend():
    backend = os.environ.get("SCP_TERMINAL_SPEECH_BACKEND", "").strip().lower()
    return backend if backend in BACKENDS or backend == "off" else None


def _warn(message):
    global _warning_shown
    if _warning_shown and not _debug_enabled():
        return

    _warning_shown = True
    print(f"[speech disabled] {message}")


def _sanitize_text(text):
    clean = str(text)
    clean = re.sub(r"\s+", " ", clean)
    clean = clean.replace("SCP-", "S C P ")
    clean = clean.replace("O5", "O five")
    return clean.strip()


def _split_text(text):
    words = text.split()
    chunks = []
    current = []
    current_length = 0

    for word in words:
        next_length = current_length + len(word) + 1
        if current and next_length > MAX_CHUNK_LENGTH:
            chunks.append(" ".join(current))
            current = [word]
            current_length = len(word)
        else:
            current.append(word)
            current_length = next_length

    if current:
        chunks.append(" ".join(current))

    return chunks


def _reset_engine():
    global _engine
    if _engine is not None:
        try:
            _engine.stop()
        except Exception:
            pass
    _engine = None


def _get_pyttsx3_engine():
    global _engine
    if _engine is not None:
        return _engine

    import pyttsx3

    driver = "sapi5" if os.name == "nt" else None
    _engine = pyttsx3.init(driver)
    _engine.setProperty("rate", DEFAULT_RATE)

    voices = _engine.getProperty("voices") or []
    if voices:
        voice_index = 3 if len(voices) > 3 else 0
        _engine.setProperty("voice", voices[voice_index].id)

    return _engine


def _speak_with_pyttsx3(chunks):
    engine = _get_pyttsx3_engine()
    for chunk in chunks:
        engine.say(chunk)
    engine.runAndWait()


def _speak_with_powershell(chunks):
    if os.name != "nt":
        raise RuntimeError("PowerShell speech is only available on Windows.")

    script = (
        "$voice = New-Object -ComObject SAPI.SpVoice; "
        "$voices = $voice.GetVoices(); "
        "if ($voices.Count -gt 0) { $voice.Voice = $voices.Item(0) }; "
        "[void]$voice.Speak($env:SCP_TERMINAL_SPEAK_TEXT)"
    )

    for chunk in chunks:
        env = os.environ.copy()
        env["SCP_TERMINAL_SPEAK_TEXT"] = chunk
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", script],
            env=env,
            capture_output=True,
            text=True,
            timeout=45,
        )
        if result.returncode != 0:
            error = result.stderr.strip() or result.stdout.strip()
            raise RuntimeError(error or "PowerShell speech failed.")


def _speak_with_gtts(chunks):
    os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")
    warnings.filterwarnings(
        "ignore",
        message="pkg_resources is deprecated as an API.*",
        category=UserWarning,
        module="pygame.pkgdata",
    )

    import pygame
    from gtts import gTTS

    for chunk in chunks:
        audio_path = None
        try:
            fd, audio_path = tempfile.mkstemp(prefix="scp-terminal-speech-", suffix=".mp3")
            os.close(fd)

            gTTS(text=chunk, lang="en").save(audio_path)

            if not pygame.mixer.get_init():
                pygame.mixer.init()
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

            pygame.mixer.music.unload()
        finally:
            if audio_path and os.path.exists(audio_path):
                try:
                    os.remove(audio_path)
                except OSError:
                    pass


def _backend_order():
    configured = _configured_backend()
    if configured == "off":
        return []
    if configured:
        return [configured]
    if _preferred_backend:
        return [_preferred_backend]
    return list(BACKENDS)


def _speak_with_backend(backend, chunks):
    if backend == "pyttsx3":
        _speak_with_pyttsx3(chunks)
    elif backend == "powershell":
        _speak_with_powershell(chunks)
    elif backend == "gtts":
        _speak_with_gtts(chunks)
    else:
        raise RuntimeError(f"Unknown speech backend: {backend}")


def speak(talk):
    global _preferred_backend

    text = _sanitize_text(talk)
    if not text:
        return False

    chunks = _split_text(text)

    with _engine_lock:
        last_error = None
        for backend in _backend_order():
            if backend in _disabled_backends:
                continue

            try:
                _speak_with_backend(backend, chunks)
                _preferred_backend = backend
                return True
            except Exception as error:
                last_error = error
                _disabled_backends.add(backend)
                if backend == "pyttsx3":
                    _reset_engine()
                if _debug_enabled():
                    print(f"[speech backend failed: {backend}] {error}")

        if last_error is not None:
            _warn(last_error)
        return False


if __name__ == "__main__":
    if speak("SCP Foundation Terminal speech test. If you can hear this, speech is working."):
        print("Speech test completed.")
