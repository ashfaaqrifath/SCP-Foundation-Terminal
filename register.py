import os

import colorama
from colorama import Back, Fore

from speech_engine import speak

colorama.init(autoreset=True)

USER_FOLDER = "Users"


def usr_register():
    os.makedirs(USER_FOLDER, exist_ok=True)

    print("")
    print(Fore.RED + "       --------------------------------")
    print(Fore.RED + "       INITIATING REGISTRATION PROCEDURE")
    print(Fore.RED + "       --------------------------------")
    speak("INITIATING REGISTRATION PROCEDURE")

    usr_name = input("       Enter username: ").strip()
    level = int(input("       Enter clearance level (0 - 5): "))
    usr_title = input("       Enter staff title: ").strip()
    usr_site = int(input("       Enter working site: "))
    usr_pass = input("       Create a password: ").strip()

    user_path = os.path.join(USER_FOLDER, f"{usr_name}.txt")
    with open(user_path, "w", encoding="utf-8") as reg:
        reg.write(f"Name : {usr_name}\n")
        reg.write(f"Clearance level : {level}\n")
        reg.write(f"Staff title : {usr_title}\n")
        reg.write(f"Working site : {usr_site}\n")
        reg.write(usr_pass)

    print("")
    print("      ", Fore.BLACK + Back.GREEN + " New user registered ")
    print(Fore.GREEN + "       You now have access to the foundation database.")
    speak("New user registered")
    speak("You now have access to the foundation database")
    return usr_name


if __name__ == "__main__":
    usr_register()
