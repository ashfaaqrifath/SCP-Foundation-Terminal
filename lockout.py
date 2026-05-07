import os
import time

import colorama
from colorama import Back, Fore

from speech_engine import speak

colorama.init(autoreset=True)


def progress(percent=0, width=30):
    symbol = width * percent // 100
    blanks = width - symbol
    print(
        "\r[ ",
        Fore.GREEN + symbol * "#",
        blanks * " ",
        " ]",
        f" {percent:.0f}%",
        sep="",
        end="",
        flush=True,
    )


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def lock_protocol():
    clear_terminal()

    for _ in range(9):
        print("")

    print(
        Fore.RED
        + """
                TERMINAL LOCKER
                ----------------
                EMERGENCY FOUNDATION ACCESS CONTROL
        """
    )
    print("")
    print("                                ", Back.RED + " << EMERGENCY LOCKOUT PROTOCOL INITIATED >> ")
    speak("EMERGENCY LOCKOUT PROTOCOL INITIATED")

    print("")
    o5_code = input(Fore.RED + "       Enter O5 authorization code: ").strip()
    if o5_code == "200211":
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

        clear_terminal()
        print("")
        print("      ", Fore.BLACK + Back.GREEN + " TERMINAL UNLOCKED ")
        return 1

    print("")
    print("      ", Fore.BLACK + Back.RED + " INVALID AUTHORIZATION CODE ")
    speak("Invalid authorization code")
    print(Fore.RED + "       << TERMINAL LOCKED >>")
    time.sleep(7300)
    return 0
