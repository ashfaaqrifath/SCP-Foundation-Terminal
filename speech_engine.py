import pyttsx3


def speak(talk):
    engine = pyttsx3.init("sapi5")
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(talk)
    engine.runAndWait()






# <<< Copyright (c) 2023 Ashfaaq Rifath - SCP Foundation Terminal v2.1.1 >>>