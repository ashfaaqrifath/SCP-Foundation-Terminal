import pyttsx3

def speak(talk):
    engine = pyttsx3.init("sapi5")
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[3].id)
    engine.say(talk)
    engine.runAndWait()