import colorama
import requests
from bs4 import BeautifulSoup
import scp001
import register
import time
from SpeechEngine import casper_speak
from lockout import lock_protocol
import subprocess
import os
import os.path
import shutil
import sys
from colorama import Fore, Back
colorama.init(autoreset=True)


def progress(percent=0, width=30):
    symbol = width * percent // 100
    blanks = width - symbol
    print('\r[ ', Fore.GREEN + symbol * "█", blanks*' ', ' ]', f' {percent:.0f}%', sep='', end='', flush=True)

print("")
print(Fore.YELLOW + "       Connecting SCP terminal")
for i in range(101):
    progress(i)
    time.sleep(0.01)

print()
print(Fore.GREEN + "           Systems online")
time.sleep(1)
os.system('cls')

print("")
print('''
                 █▀▀▀█  █▀▀█  █▀▀█   █▀▀▀  █▀▀▀█  █  █  █▄  █  █▀▀▄  █▀▀█ ▀▀█▀▀ ▀█▀  █▀▀▀█  █▄  █ 
                 ▀▀▀▄▄  █     █▄▄█   █▀▀▀  █   █  █  █  █ █ █  █  █  █▄▄█   █    █   █   █  █ █ █ 
                 █▄▄▄█  █▄▄█  █      █     █▄▄▄█  █▄▄█  █  ▀█  █▄▄▀  █  █   █   ▄█▄  █▄▄▄█  █  ▀█
                                    SECURE   ●   CONTAIN   ●   PROTECT''')
print("")
print("         ", Back.RED + " WARNING. THE SCP FOUNDATION DATABASE IS CLASSIFIED. UNAUTHORIZED ACCESS IS STRICTLY PROHIBITED ")
#casper_speak("WARNING. THEE SCP FOUNDATION DATABASE IS CLASSIFIED. UNAUTHORIZED ACCESS IS STRICTLY PROHIBITED.")
print("")

login_name = input("       Enter username: ")
if login_name == "override":
    subprocess.call("override.py", shell=True)

login_pass = input("       Enter password: ")

print(Fore.YELLOW + "       Verifying credentials...")
casper_speak("Verifying credentials")
time.sleep(0.05)

usr_file = open(f"{login_name}.txt")

with open(f"{login_name}.txt") as p:
    if login_pass in p.read():
        
        print("      ", Fore.BLACK + Back.GREEN + " ACCESS GRANTED ")
        casper_speak("Access granted.")

        folder = os.path.exists("SCP object files")
        if folder == False:
            os.mkdir("SCP object files")
        elif folder == True:
            pass

        if __name__ == "__main__":

            while(1):
                print("")
                casper_speak("Enter terminal command")
                usr = input("       Enter terminal command: ")

                if usr == "001":
                    scp001.restricted()

                elif usr.lower() == "del":
                    print("")
                    print(Fore.RED + "       ----------------------------")
                    print(Fore.RED + "       INITIATING DELETION PROTOCOL")
                    print(Fore.RED + "       ----------------------------")
                    casper_speak("initiating deletion protocol")
                    shutil.rmtree("SCP object files")
                    time.sleep(1)
                    print(Fore.GREEN + "       All files related to SCP objects has been deleted.")
                    casper_speak("All files related to SCP objects has been deleted")

                elif usr == "help":
                    print("")
                    print("        -----------------------------------------")
                    print("       |", Fore.CYAN + "Enter SCP item number :", Fore.LIGHTBLACK_EX + "Displays information for a given artifact")
                    print("       |", Fore.CYAN + "del :", Fore.LIGHTBLACK_EX + "Initiates deletion protocol")
                    print("       |", Fore.CYAN + "lock :", Fore.LIGHTBLACK_EX + "Initiates emergency lockout protocol")
                    print("       |", Fore.CYAN + "clear :", Fore.LIGHTBLACK_EX + "Clears the output of the terminal")
                    print("       |", Fore.CYAN + "reg :", Fore.LIGHTBLACK_EX + "Registers new user")
                    print("       |", Fore.CYAN + "usr :", Fore.LIGHTBLACK_EX + "Displays user information")
                    print("        -----------------------------------------")
                    time.sleep(3)

                elif usr == "lock":
                    lock_protocol()

                elif usr == "reg":
                    register.usr_register()
                    
                elif usr == "clear":
                    os.system('cls')
                    casper_speak("terminal output cleared")

                elif usr == "exit":
                    break

                else:
                    r = requests.get(f'https://scp-wiki.wikidot.com/scp-{usr}')
                    soup = BeautifulSoup(r.content, 'html.parser')
                    s = soup.find('div', id='page-content')

                    paras = len(s.find_all("p"))

                    print("")
                    print(Fore.YELLOW + f"   Accessing SCP-{usr} files")
                    casper_speak(f"Accessing SCP-{usr} files")
                    for i in range(101):
                        progress(i)
                        time.sleep(0.01)

                    print()
                    print(Fore.GREEN + "        Access granted")
                    print("")

                    print(Fore.GREEN + soup.title.text.center(100))
                    print("")

                    paras_num = range(1, paras)
                    num_list = list(paras_num)

                    item = f"{s.find_all('p')[0].text}\n"
                    print(Fore.YELLOW + item.center(100))


                    try:
                        for i in num_list:
                            txt = s.find_all('p')[i].text

                            def format_paragraph(paragraph, length, left, right):
                                words = paragraph.split()
                                lines = []
                                curline = '         ' * (left - 1)  # we add a space before the first word

                                while words:
                                    word = words.pop(0)  # process the next word
                                    # +1 in the next line is for the space.
                                    if len(curline) + 1 + len(word) > length - right:
                                        # line would have been too long, start a new line
                                        lines.append(curline)
                                        curline = '         ' * (left - 1)
                                    curline += " " + word
                                lines.append(curline)

                                return '\n'.join(lines)
                            # we need to work on one paragraph at a time
                            paragraphs = txt.split('\n\n')

                            for paragraph in paragraphs:
                                q = format_paragraph(paragraph, 80, left=4, right=5)
                                print(q)
                                print("")  # next paragraph

                    except IndexError:
                        print(Fore.RED + "<<< END OF FILE >>>".center(100))
                    print(Fore.RED + "<<< END OF FILE >>>".center(100))
                    print(Fore.LIGHTBLACK_EX + "File saved locally".center(100))
                    print("")
                    print(Fore.LIGHTBLACK_EX + "Terminal developed by @ashfaaqrifath".center(100))

                    save_path = "SCP object files"
                    save = os.path.join(save_path, f'SCP-{usr}.txt')

                    orig_stdout = sys.stdout
                    f = open(save, 'w', encoding="utf-8")
                    sys.stdout = f

                    for i in num_list:
                        txt = s.find_all('p')[i].text

                        def format_paragraph(paragraph, length, left, right):
                            words = paragraph.split()
                            lines = []
                            curline = '         ' * (left - 1)  # we add a space before the first word

                            while words:
                                word = words.pop(0)  # process the next word
                                    # +1 in the next line is for the space.
                                if len(curline) + 1 + len(word) > length - right:
                                        # line would have been too long, start a new line
                                    lines.append(curline)
                                    curline = '         ' * (left - 1)
                                curline += " " + word
                            lines.append(curline)

                            return '\n'.join(lines)
                            # we need to work on one paragraph at a time
                        paragraphs = txt.split('\n\n')

                        for paragraph in paragraphs:
                            q = format_paragraph(paragraph, 80, left=4, right=5)
                            print(q)
                            print("")

                    sys.stdout = orig_stdout
                    f.close()

                    casper_speak(f"Item number : SCP-{usr}")

                    sis = s.find_all('p')[2].text
                    casper_speak(sis)

                    lines = s.find_all('p')[3]
                    casper_speak(lines)

    else:
        print("")
        print("      ", Fore.BLACK + Back.RED + " ACCESS DENIED ")
        casper_speak("Access Denied")
        print("")
        print(Fore.RED + "       UNAUTHORIZED ACCESS DETECTED")
        print(Fore.RED + "       --------------------------------")
        print(Fore.RED + "       INITIATING TERMINATION PROTOCOL")
        print(Fore.RED + "       --------------------------------")
        casper_speak("INITIATING TERMINATION PROTOCOL")






# <<< Copyright (c) 2022 Ashfaaq Rifath - SCP Foundation Terminal v2.0.0 >>>