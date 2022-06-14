import time
import os
import colorama
from SpeechEngine import casper_speak
from colorama import Fore, Back
colorama.init(autoreset=True)

def lock_protocol():
    os.system('cls')
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print(Fore.RED + '''
                    ▀▀█▀▀  █▀▀▀  █▀▀█  █▀▄▀█ ▀█▀  █▄  █  █▀▀█  █       █     █▀▀▀█  █▀▀█  █ ▄▀  █▀▀▀  █▀▀▄ 
                      █    █▀▀▀  █▄▄▀  █ █ █  █   █ █ █  █▄▄█  █       █     █   █  █     █▀▄   █▀▀▀  █  █ 
                      █    █▄▄▄  █  █  █   █ ▄█▄  █  ▀█  █  █  █▄▄█    █▄▄█  █▄▄▄█  █▄▄█  █  █  █▄▄▄  █▄▄▀''')
    print("")
    print("                                    ", Back.RED + " <<< EMERGENCY LOCKOUT PROTOCOL INITIATED >>> ")
    casper_speak("EMERGENCY LOCKOUT PROTOCOL INITIATED")
    casper_speak("EMERGENCY LOCKOUT PROTOCOL INITIATED")
    casper_speak("EMERGENCY LOCKOUT PROTOCOL INITIATED")
    time.sleep(7200) # terminal lockout for 2 hours





# <<< Copyright (c) 2022 Ashfaaq Rifath - SCP Foundation Terminal v2.0.0 >>>