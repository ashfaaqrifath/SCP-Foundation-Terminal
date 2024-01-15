import os
import re
import sys
import os.path
import shutil
import random
import datetime
import colorama
import requests
import scp001
import register
import time
import subprocess
from bs4 import BeautifulSoup
from speech_engine import speak
from lockout import lock_protocol
from datetime import date
from chronicle_engine import chronicle_log, clean_slate
from colorama import Fore, Back
colorama.init(autoreset=True)


def progress(percent=0, width=30):
    symbol = width * percent // 100
    blanks = width - symbol
    print('\r[ ', Fore.GREEN + symbol * "█", blanks*' ', ' ]',
          f' {percent:.0f}%', sep='', end='', flush=True)

def command_engine(mode):

    folder = os.path.exists("SCP object files")
    if folder == False:
        os.mkdir("SCP object files")
    elif folder == True:
        pass

    if __name__ == "__main__":

        while(1):
            print("")
            speak("Enter terminal command")
            chronicle_log("       Enter terminal command: ", mode)
            usr = input("       Enter terminal command: ")
            chronicle_log(usr, mode)

            if usr.startswith("scp"):
                get_num = re.search(r'\d+', usr)

                if get_num:
                    item_num = get_num.group()

                    if item_num == "001":
                        chronicle_log("<< ACCESS RESTRICTED >>", mode)
                    chronicle_log("ACCESS TO SCP-001 IS RESCRICTED TO O5 COUNCIL MEMBERS ONLY.", mode)
                    scp001.restricted()
                else:
                    print("")
                    print("      ", Fore.BLACK + Back.RED + " INVALID COMMAND ")
                    print(Fore.RED + "       PLEASE TRY AGAIN")
                    speak("please try again")

            elif usr.lower() == "del":
                print(Fore.RED + "       << INITIATED CLEAN SLATE PROTOCOL >>")
                speak("INITIATED CLEAN SLATE PROTOCOL")
                try:
                    shutil.rmtree("SCP object files")
                except PermissionError:
                    pass
                time.sleep(1)
                print(
                    Fore.GREEN + "       All SCP object files has been deleted.")
                speak("All SCP object files has been deleted")
                chronicle_log("       INITIATED CLEAN SLATE PROTOCOL", mode)
                chronicle_log("       All files SCP objects files has been deleted.", mode)

            elif usr == "help":
                print("")
                print("       ●", Fore.CYAN + "Enter SCP item number :", Fore.LIGHTBLACK_EX + "Displays SCP item information")
                print("       ●", Fore.CYAN + "random :", Fore.LIGHTBLACK_EX + "Displays information for a random artifact")
                print("       ●", Fore.CYAN + "del :", Fore.LIGHTBLACK_EX + "Deletes all SCP files")
                print("       ●", Fore.CYAN + "lock :", Fore.LIGHTBLACK_EX + "Emergency lockout protocol")
                print("       ●", Fore.CYAN + "incog :", Fore.LIGHTBLACK_EX + "Incognito mode")
                print("       ●", Fore.CYAN + "dis :", Fore.LIGHTBLACK_EX + "Disable incognito mode")
                print("       ●", Fore.CYAN + "clean :", Fore.LIGHTBLACK_EX + "Deletes all activity log files")
                print("       ●", Fore.CYAN + "clear :", Fore.LIGHTBLACK_EX + "Clears all terminal output")
                print("       ●", Fore.CYAN + "reg :", Fore.LIGHTBLACK_EX + "Registers new user")
                print("       ●", Fore.CYAN + "profile :", Fore.LIGHTBLACK_EX + "Displays user information")
                print("       ●", Fore.CYAN + "exit :", Fore.LIGHTBLACK_EX + "Closes the terminal")
                speak("Displaying terminal instructions.")
                chronicle_log("Displaying terminal instructions.", mode)
                time.sleep(1)

            elif usr == "lock":
                chronicle_log("       << EMERGENCY LOCKOUT PROTOCOL INITIATED >> ", mode)
                lock_protocol()

            elif usr == "incog":
                chronicle_log("       << ENABLED INCOGNITO MODE >>", mode)
                print(Fore.RED + "       << ENABLED INCOGNITO MODE >>")
                speak("ENABLED INCOGNITO MODE")
                mode = 1

            elif usr == "dis":
                chronicle_log("       << DISABLED INCOGNITO MODE >>", mode)
                print(Fore.GREEN + "       << DISABLED INCOGNITO MODE >>")
                speak("DISABLED INCOGNITO MODE")
                mode = 0

            elif usr == "clean":
                print(Fore.RED + "       << INITIATED CLEAN SLATE PROTOCOL >>")
                speak("INITIATED CLEAN SLATE PROTOCOL")
                clean_slate()
                mode = 1
                print(Fore.GREEN + "       All activity log files has been deleted")
                speak("All activity log files has been deleted")

            elif usr == "reg":
                chronicle_log("       INITIATING REGISTRATION PROCEDURE", mode)
                register.usr_register()

            elif usr == "profile":
                try:
                    usr_file2 = open(f"Users/{login_name}.txt")
                    content = usr_file2.readlines()
                    print("")
                    print(Fore.CYAN + "          --------------")
                    print(Fore.YELLOW + f"          USER PROFILE")
                    print(Fore.CYAN + "          --------------")
                    print("       ● ", Fore.CYAN + content[0], end="")
                    print("       ● ", Fore.CYAN + content[1], end="")
                    print("       ● ", Fore.CYAN + content[2], end="")
                    print("       ● ", Fore.CYAN + content[3], end="")

                    speak(content[0])
                    speak(content[1])
                    speak(content[2])
                    speak(content[3])
                    usr_file2.close()

                    chronicle_log(f"          USER PROFILE", mode)
                    chronicle_log(f"       ● {content[0]}", mode)
                    chronicle_log(f"       ● {content[1]}", mode)
                    chronicle_log(f"       ● {content[2]}", mode)
                    chronicle_log(f"       ● {content[3]}", mode)
                    time.sleep(1)
                except (FileNotFoundError, UnboundLocalError) as e:
                    print(Fore.RED + "       User data not found")
                    speak("User data not found")

            elif usr == "random":
                random_scp = random.randint(1, 7100)

                r = requests.get(f'https://scp-wiki.wikidot.com/scp-{random_scp}')
                soup = BeautifulSoup(r.content, 'html.parser')
                s = soup.find('div', id='page-content')
                paras = len(s.find_all("p"))

                print("")
                print(Fore.YELLOW + f"     Accessing SCP-{random_scp} files")
                speak(f"Accessing SCP-{random_scp} files")
                chronicle_log(f"     Accessing SCP-{random_scp} files", mode)
                for i in range(101):
                    progress(i)
                    time.sleep(0.01)

                print()
                print(Fore.GREEN + "        Access granted")
                chronicle_log("        Access granted", mode)
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
                            # we add a space before the first word
                            curline = '         ' * (left - 1)

                            while words:
                                # process the next word
                                word = words.pop(0)
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
                            q = format_paragraph(
                                paragraph, 80, left=4, right=5)
                            print(q)
                            print("")  # next paragraph

                except IndexError:
                    print(Fore.RED + "<< END OF FILE >>".center(100))
                print(Fore.RED + "<< END OF FILE >>".center(100))
                print(Fore.LIGHTBLACK_EX + "File saved locally".center(100))
                chronicle_log("<< File saved locally >>".center(100), mode)
                print("")
                print(Fore.LIGHTBLACK_EX +
                    "Copyright © 2024 Ashfaaq Rifath".center(100))

                save_path = "SCP object files"
                save = os.path.join(save_path, f'SCP-{random_scp}.txt')

                orig_stdout = sys.stdout
                f = open(save, 'w', encoding="utf-8")
                sys.stdout = f

                for i in num_list:
                    txt = s.find_all('p')[i].text

                    def format_paragraph(paragraph, length, left, right):
                        words = paragraph.split()
                        lines = []
                        # we add a space before the first word
                        curline = '         ' * (left - 1)

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
                        q = format_paragraph(
                            paragraph, 80, left=4, right=5)
                        print(q)
                        print("")
                sys.stdout = orig_stdout
                f.close()

                speak(f"Item number : SCP-{random_scp}")
                sis = s.find_all('p')[2].text
                speak(sis)

                lines = s.find_all('p')[3]
                speak(lines)

            elif usr == "clear":
                os.system('cls')
                speak("terminal output cleared")
                chronicle_log("     Terminal output cleared", mode)

            elif usr == "exit":
                chronicle_log("END LOG >>", mode)
                break

            elif usr.startswith("scp"):
                get_num = re.search(r'\d+', usr)

                if get_num:
                    item_num = get_num.group()
                else:
                    print("")
                    print("      ", Fore.BLACK + Back.RED + " INVALID COMMAND ")
                    print(Fore.RED + "       PLEASE TRY AGAIN")
                    speak("please try again")

                r = requests.get(f'https://scp-wiki.wikidot.com/scp-{item_num}')
                soup = BeautifulSoup(r.content, 'html.parser')
                s = soup.find('div', id='page-content')

                paras = len(s.find_all("p"))

                print("")
                print(Fore.YELLOW + f"     Accessing SCP-{item_num} files")
                speak(f"Accessing SCP-{item_num} files")
                chronicle_log(f"     Accessing SCP-{item_num} files", mode)
                for i in range(101):
                    progress(i)
                    time.sleep(0.01)

                print()
                print(Fore.GREEN + "        Access granted")
                chronicle_log("        Access granted", mode)
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
                            # we add a space before the first word
                            curline = '         ' * (left - 1)

                            while words:
                                # process the next word
                                word = words.pop(0)
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
                    print(Fore.RED + "<< END OF FILE >>".center(100))
                print(Fore.RED + "<< END OF FILE >>".center(100))
                print(Fore.LIGHTBLACK_EX + "File saved locally".center(100))
                chronicle_log("<< File saved locally >>".center(100), mode)
                print("")
                print(Fore.LIGHTBLACK_EX +
                    "Copyright © 2024 Ashfaaq Rifath".center(100))

                save_path = "SCP object files"
                save = os.path.join(save_path, f'SCP-{item_num}.txt')

                orig_stdout = sys.stdout
                f = open(save, 'w', encoding="utf-8")
                sys.stdout = f

                for i in num_list:
                    txt = s.find_all('p')[i].text

                    def format_paragraph(paragraph, length, left, right):
                        words = paragraph.split()
                        lines = []
                        # we add a space before the first word
                        curline = '         ' * (left - 1)

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
                        q = format_paragraph(
                            paragraph, 80, left=4, right=5)
                        print(q)
                        print("")

                sys.stdout = orig_stdout
                f.close()

                speak(f"Item number : SCP-{item_num}")

                sis = s.find_all('p')[2].text
                speak(sis)

                lines = s.find_all('p')[3]
                speak(lines)

            else:
                print("")
                print("      ", Fore.BLACK + Back.RED + " INVALID COMMAND ")
                print(Fore.RED + "       PLEASE TRY AGAIN")
                speak("please try again")

###########################################################################

print("")
print(Fore.YELLOW + "      Connecting SCP terminal")

# for i in range(101):
#     progress(i)
#     time.sleep(0.01)

print()
print(Fore.GREEN + "           Systems online")
print("")
print(Fore.LIGHTBLACK_EX +
      "Copyright © 2024 Ashfaaq Rifath - SCP Foundation Terminal v2.1.4")
time.sleep(1)
os.system('cls')

incognito = 0

date = datetime.datetime.now().strftime("%D:%h:%H:%M:%S")
chronicle_log(write="SCP Foundation Terminal v2.1.4\n" +
           str(date) + " \n<< ACTIVITY LOG >> \nBEGIN LOG >>\n \n", incog=incognito)

print("")
print('''
                 █▀▀▀█  █▀▀█  █▀▀█   █▀▀▀  █▀▀▀█  █  █  █▄  █  █▀▀▄  █▀▀█ ▀▀█▀▀ ▀█▀  █▀▀▀█  █▄  █ 
                 ▀▀▀▄▄  █     █▄▄█   █▀▀▀  █   █  █  █  █ █ █  █  █  █▄▄█   █    █   █   █  █ █ █ 
                 █▄▄▄█  █▄▄█  █      █     █▄▄▄█  █▄▄█  █  ▀█  █▄▄▀  █  █   █   ▄█▄  █▄▄▄█  █  ▀█
                                    SECURE   ●   CONTAIN   ●   PROTECT''')
print("")
print("         ", Back.RED + " WARNING. THE SCP FOUNDATION DATABASE IS CLASSIFIED. UNAUTHORIZED ACCESS IS STRICTLY PROHIBITED ")
#speak("WARNING. THEE SCP FOUNDATION DATABASE IS CLASSIFIED. UNAUTHORIZED ACCESS IS STRICTLY PROHIBITED.")
print("")

attempts = 3

while attempts > 0:

    login_name = input("       Enter username: ")
    if login_name == "override":
        login_name = "override"
        chronicle_log("<< TERMINAL OVERRIDE >>", incognito)
        chronicle_log("END LOG >>", incognito)
        incognito = 1

        print(Fore.RED + "       << TERMINAL OVERRIDE >>")
        print("")
        speak("Enter security override code")
        login_pass = input(Fore.RED + "       Enter security override code: ")

    else:
        login_pass = input("       Enter password: ")

    print(Fore.YELLOW + "       Verifying credentials...")
    time.sleep(1.5)

    if login_name == "override":
        p = "2002"

        if login_pass != p:
            print("")
            print("      ", Fore.BLACK + Back.RED + " INVALID OVERRIDE CODE ")
            speak("INVALID OVERRIDE CODE")
            chronicle_log("       << EMERGENCY LOCKOUT PROTOCOL INITIATED >> ", incognito)
            o5_code = lock_protocol()

    else:
        try:
            p = " "
            usr_file = open(f"Users/{login_name}.txt")
            p = usr_file.readlines()[4]
        except FileNotFoundError:
            pass

    o5_code = 0

    if login_pass in p and len(login_pass) == 4 or o5_code == 1:

        if o5_code != 1 and login_name != "override":
            print("      ", Fore.BLACK + Back.GREEN + " ACCESS GRANTED ")
            speak("Access granted.")

            print("")
            print(Fore.GREEN + f"       Welcome {login_name}")
            speak(f"       Welcome {login_name}")
            chronicle_log(f"       Welcome {login_name}", incognito)
        
        elif login_name == "override":
            print(Fore.GREEN + "       Override code accepted")
            speak("Override code accepted")

        command_engine(incognito)
        break

    else:
        attempts -= 1
        print("")
        print("      ", Fore.BLACK + Back.RED + " INVALID CREDENTIALS ")
        print(Fore.RED + "       PLEASE TRY AGAIN")
        speak("INVALID CREDENTIALS")
        print()

if attempts == 0:
    print("")
    print("      ", Fore.BLACK + Back.RED + " ACCESS DENIED ")
    speak("Access Denied")
    chronicle_log("       << EMERGENCY LOCKOUT PROTOCOL INITIATED >> ", incognito)
    o5_code = lock_protocol()
    if o5_code == 1:
        command_engine(incognito)


# Copyright (c) 2024 Ashfaaq Rifath - SCP Foundation Terminal v2.1.4