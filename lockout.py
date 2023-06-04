import time
import os
import colorama
from speech_engine import speak
from colorama import Fore, Back
colorama.init(autoreset=True)


def progress(percent=0, width=30):
    symbol = width * percent // 100
    blanks = width - symbol
    print('\r[ ', Fore.GREEN + symbol * "█", blanks*' ', ' ]', f' {percent:.0f}%', sep='', end='', flush=True)


def lock_protocol():
    os.system('cls')

    for x in range(9):
        print("")

    print(Fore.RED + '''
                ▀▀█▀▀  █▀▀▀  █▀▀█  █▀▄▀█ ▀█▀  █▄  █  █▀▀█  █       █     █▀▀▀█  █▀▀█  █ ▄▀  █▀▀▀  █▀▀▄ 
                  █    █▀▀▀  █▄▄▀  █ █ █  █   █ █ █  █▄▄█  █       █     █   █  █     █▀▄   █▀▀▀  █  █ 
                  █    █▄▄▄  █  █  █   █ ▄█▄  █  ▀█  █  █  █▄▄█    █▄▄█  █▄▄▄█  █▄▄█  █  █  █▄▄▄  █▄▄▀''')
    print("")
    print("                                ", Back.RED + " <<< EMERGENCY LOCKOUT PROTOCOL INITIATED >>> ")
    for y in range(2):
        speak("EMERGENCY LOCKOUT PROTOCOL INITIATED")

    print("")
    me = input(Fore.RED + "       Enter O5 authorization code: ")
    if me == "200211":
        print("")
        print(Fore.YELLOW + "    Bypassing lockout protocol")
        for i in range(101):
            progress(i)
            time.sleep(0.01)

        print()
        print(Fore.GREEN + "    Lockout protocol disabled")
        print("")
        print(Fore.GREEN + "  O5 authorization code accepted")
        speak("lockout protocol disabled")

        os.system('cls')
        print("")
        print("      ", Fore.BLACK + Back.GREEN + " TERMINAL UNLOCKED ")
        speak("TERMINAL UNLOCKED")

    else:
        print("")
        print("      ", Fore.BLACK + Back.RED + " INVALID AUTHORIZATION CODE ")
        speak("Invalid authorization code")
        time.sleep(7200)