import time
import os
import colorama
from speech_engine import speak
from colorama import Fore, Back
colorama.init(autoreset=True)


def progress(percent=0, width=30):
    symbol = width * percent // 100
    blanks = width - symbol
    print('\r[ ', Fore.GREEN + symbol * "█", blanks*' ', ' ]',
          f' {percent:.0f}%', sep='', end='', flush=True)


def lock_protocol():
    os.system('cls')

    for x in range(9):
        print("")

    print(Fore.RED + '''
                ▀▀█▀▀ █▀▀▀  █▀▀█  █▀▄▀█ ▀█▀  █▄  █  █▀▀█  █       █     █▀▀▀█  █▀▀█  █ ▄▀  █▀▀▀  █▀▀▄ 
                  █   █▀▀▀  █▄▄▀  █ █ █  █   █ █ █  █▄▄█  █       █     █   █  █     █▀▄   █▀▀▀  █  █ 
                  █   █▄▄▄  █  █  █   █ ▄█▄  █  ▀█  █  █  █▄▄█    █▄▄█  █▄▄▄█  █▄▄█  █  █  █▄▄▄  █▄▄▀''')
    print("")
    print("                                ", Back.RED + " << EMERGENCY LOCKOUT PROTOCOL INITIATED >> ")
    speak("EMERGENCY LOCKOUT PROTOCOL INITIATED")

    print("")
    O5 = input(Fore.RED + "       Enter O5 authorization code: ")
    if O5 == "200211":
        print("")
        print(Fore.YELLOW + "    Bypassing lockout protocol")
        for i in range(101):
            progress(i)
            time.sleep(0.0001)

        print()
        print(Fore.GREEN + "    Lockout protocol disabled")
        print("")
        print(Fore.GREEN + "  O5 authorization code accepted")
        speak("O5 authorization code accepted")
        #speak("lockout protocol disabled")

        os.system('cls')
        print("")
        print("      ", Fore.BLACK + Back.GREEN + " TERMINAL UNLOCKED ")
        terminal = 1
        return terminal

    else:
        print("")
        print("      ", Fore.BLACK + Back.RED + " INVALID AUTHORIZATION CODE ")
        speak("Invalid authorization code")
        print(Fore.RED + "       << TERMINAL LOCKED >>")
        time.sleep(7300)
