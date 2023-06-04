import time
import pyttsx3
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)


def casper_speak(talk):
    engine = pyttsx3.init("sapi5")
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(talk)
    engine.runAndWait()


def restricted():
    print("")
    print("                                    ", Back.RED + " <<< ACCESS RESTRICTED >>> ")
    print(Fore.RED + "--------------------------------------------------------------------------".center(100))
    print(Fore.RED + "THIS FILE HAS BEEN CLASSIFIED".center(100))
    print(Fore.RED + "<<< TOP SECRET >>>".center(100))
    print(Fore.RED + "BY ORDER OF THE ADMINISTRATOR".center(100))
    print("")
    print(Fore.RED + "ACCESS TO SCP-001 IS RESCRICTED TO O5 COUNCIL MEMBERS ONLY.".center(100))
    print(Fore.RED + "--------------------------------------------------------------------------".center(100))
    print("")

    print(Fore.YELLOW + "GENERAL NOTICE 001-ALPHA:".center(100))
    print(Fore.YELLOW + "IN ORDER TO PREVENT KNOWLEDGE OF SCP-001 FROM".center(100))
    print(Fore.YELLOW + "BEING LEAKED, SEVERAL/NO FALSE SCP-001 FILES".center(100))
    print(Fore.YELLOW + "HAVE BEEN CREATED ALONGSIDE THE TRUE FILE/FILES.".center(100))
    print(Fore.YELLOW + "ALL FILES CONCERNING THE NATURE OF SCP-001, INCLUDING".center(100))
    print(Fore.YELLOW + "THE DECOY/DECOYS, ARE PROTECTED".center(100))
    print(Fore.YELLOW + "BY A MEMETIC KILL AGENT DESIGNED TO IMMEDIATELY".center(100))
    print(Fore.YELLOW + "CAUSE CARDIAC ARREST IN ANY NONAUTHORIZED PERSONNEL".center(100))
    print(Fore.YELLOW + "ATTEMPTING TO ACCESS THE FILE. REVEALING THE TRUE NATURE/NATURES OF SCP-001".center(100))
    print(Fore.YELLOW + "TO THE GENERAL PUBLIC IS CAUSE FOR EXECUTION.".center(100))
    print(Fore.YELLOW + "EXCEPT AS REQUIRED UNDER ████-███-██████.".center(100))
    print("")

    print(Fore.RED + "--------------------------------------------------------------------------".center(100))
    print(Fore.RED + "ANY NON-AUTHORIZED PERSONNEL ACCESSING THESE DOCUMENTS WILL BE IMMEDIATELY".center(100))
    print(Fore.RED + "TERMINATED THROUGH THE BERRYMAN-LANGFORD MEMETIC KILL AGENT.".center(100))
    print(Fore.RED + "--------------------------------------------------------------------------".center(100))
    print("")
    print(Fore.LIGHTBLACK_EX + "Terminal developed by Ashfaaq Rifath".center(100))

    casper_speak("ACCESS DENIED")
    casper_speak("ACCESS TO SCP-001 is restricted TO O-five COUNCIL MEMBERS ONLY.")
    casper_speak("unauthorized personal access will be terminated through a memetic kill agent.")
    casper_speak("this file has been classified as top secret by order of the administrator.")
    time.sleep(1)
    print("")