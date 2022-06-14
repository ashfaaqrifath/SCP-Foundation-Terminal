import sys
from SpeechEngine import casper_speak
from colorama import Fore, Back
import colorama
colorama.init(autoreset=True)

def usr_register():
    print("")
    print(Fore.RED + "       --------------------------------")
    print(Fore.RED + "       INITIATING REGISTRATION PROTOCOL")
    print(Fore.RED + "       --------------------------------")
    casper_speak("INITIATING REGISTRATION PROTOCOL")

    usr_name = input("       Enter username: ")
    level = input("       Enter clearance level (0 - 5): ")
    usr_tile = input("       Enter staff title: ")
    usr_site = input("       Enter working site: ")
    usr_pass = input("       Create a password: ")
                
    usrReg = sys.stdout
    reg = open(f'{usr_name}.txt', 'w', encoding="utf-8")
    sys.stdout = reg

    print(f"Name : {usr_name}")
    print(f"Clearance level : {level}")
    print(f"Staff title : {usr_tile}")
    print(f"Working site : {usr_site}")
    print(usr_pass)
    
    sys.stdout = usrReg
    reg.close()

    print("")
    print("      ", Fore.BLACK + Back.GREEN + " New user registered ")
    print(Fore.GREEN + "       You now have access to the foundation database.")
    casper_speak("New user registered")
    casper_speak("You now have access to the foundation database")







# <<< Copyright (c) 2022 Ashfaaq Rifath - SCP Foundation Terminal v2.0.0 >>>