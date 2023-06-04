import os
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

print("")
print(Fore.YELLOW + "      Connecting SCP terminal")
for i in range(101):
    progress(i)
    time.sleep(0.01)

print()
print(Fore.GREEN + "           Systems online")
print("")
print(Fore.LIGHTBLACK_EX +
      "Copyright © 2023 Ashfaaq Rifath - SCP Foundation Terminal v2.1.3")
time.sleep(1)
os.system('cls')

incognito = 0

date = datetime.datetime.now().strftime("%D:%h:%H:%M:%S")
chronicle_log(write="SCP Foundation Terminal v2.1.3\n" +
           str(date) + " \n<<< ACTIVITY LOG >>> \nBEGIN LOG >>>\n \n", incog=incognito)

print("")
print('''
                 █▀▀▀█  █▀▀█  █▀▀█   █▀▀▀  █▀▀▀█  █  █  █▄  █  █▀▀▄  █▀▀█ ▀▀█▀▀ ▀█▀  █▀▀▀█  █▄  █ 
                 ▀▀▀▄▄  █     █▄▄█   █▀▀▀  █   █  █  █  █ █ █  █  █  █▄▄█   █    █   █   █  █ █ █ 
                 █▄▄▄█  █▄▄█  █      █     █▄▄▄█  █▄▄█  █  ▀█  █▄▄▀  █  █   █   ▄█▄  █▄▄▄█  █  ▀█
                                    SECURE   ●   CONTAIN   ●   PROTECT''')
print("")
print("         ", Back.RED + " WARNING. THE SCP FOUNDATION DATABASE IS CLASSIFIED. UNAUTHORIZED ACCESS IS STRICTLY PROHIBITED ")
speak("WARNING. THEE SCP FOUNDATION DATABASE IS CLASSIFIED. UNAUTHORIZED ACCESS IS STRICTLY PROHIBITED.")
print("")

login_name = input("       Enter username: ")
if login_name == "override":
    chronicle_log("<<< TERMINAL OVERRIDE >>>", incognito)
    chronicle_log("END LOG >>>", incognito)
    incognito = 1
    subprocess.call("override.py", shell=True)

login_pass = input("       Enter password: ")

print(Fore.YELLOW + "       Verifying credentials...")
time.sleep(1.5)

if len(login_pass) == 4:
    try:
        usr_file = open(f"Users/{login_name}.txt")
    except FileNotFoundError:
        print("")
        print("      ", Fore.BLACK + Back.RED + " INVALID CREDENTIALS ")
        speak("INVALID CREDENTIALS")
        print("")
        print(Fore.RED + "       UNAUTHORIZED ACCESS DETECTED")
        print(Fore.RED + "       --------------------------------")
        print(Fore.RED + "       INITIATING TERMINATION PROTOCOL")
        print(Fore.RED + "       --------------------------------")
        speak("INITIATING TERMINATION PROTOCOL")

    p = usr_file.readlines()[4]
    if login_pass in p:

        print("      ", Fore.BLACK + Back.GREEN + " ACCESS GRANTED ")
        speak("Access granted.")

        folder = os.path.exists("SCP object files")
        if folder == False:
            os.mkdir("SCP object files")
        elif folder == True:
            pass

        log_folder = os.path.exists("Activity Logs")
        if log_folder == False:
            os.mkdir("Activity Logs")
        elif log_folder == True:
            pass

        print("")
        print(Fore.GREEN + f"       Welcome {login_name}")
        speak(f"       Welcome {login_name}")
        chronicle_log(f"       Welcome {login_name}", incognito)

        if __name__ == "__main__":

            while(1):
                print("")
                speak("Enter terminal command")
                chronicle_log("       Enter terminal command: ", incognito)
                usr = input("       Enter terminal command: ")
                chronicle_log(usr, incognito)

                if usr == "001":
                    chronicle_log("<<< ACCESS RESTRICTED >>>", incognito)
                    chronicle_log("ACCESS TO SCP-001 IS RESCRICTED TO O5 COUNCIL MEMBERS ONLY.", incognito)
                    scp001.restricted()

                elif usr.lower() == "del":
                    print("")
                    print(Fore.RED + "       ----------------------------")
                    print(Fore.RED + "       INITIATING DELETION PROTOCOL")
                    print(Fore.RED + "       ----------------------------")
                    speak("initiating deletion protocol")
                    shutil.rmtree("SCP object files")
                    time.sleep(1)
                    print(
                        Fore.GREEN + "       All SCP object files has been deleted.")
                    speak("All SCP object files has been deleted")

                    chronicle_log("       INITIATING DELETION PROTOCOL", incognito)
                    chronicle_log("       All files SCP objects files has been deleted.", incognito)

                elif usr == "help":
                    print("")
                    print("        -----------------------------------------")
                    print("       |", Fore.CYAN + "Enter SCP item number :", Fore.LIGHTBLACK_EX + "Displays information for a given artifact")
                    print("       |", Fore.CYAN + "random :", Fore.LIGHTBLACK_EX + "Displays information for a random artifact")
                    print("       |", Fore.CYAN + "del :", Fore.LIGHTBLACK_EX + "Deletes all SCP files")
                    print("       |", Fore.CYAN + "lock :", Fore.LIGHTBLACK_EX + "Emergency lockout protocol")
                    print("       |", Fore.CYAN + "incog :", Fore.LIGHTBLACK_EX + "Incognito mode")
                    print("       |", Fore.CYAN + "dis :", Fore.LIGHTBLACK_EX + "Disable incognito mode")
                    print("       |", Fore.CYAN + "clean :", Fore.LIGHTBLACK_EX + "Deletes all activity log files")
                    print("       |", Fore.CYAN + "clear :", Fore.LIGHTBLACK_EX + "Clears all terminal output")
                    print("       |", Fore.CYAN + "reg :", Fore.LIGHTBLACK_EX + "Registers new user")
                    print("       |", Fore.CYAN + "profile :", Fore.LIGHTBLACK_EX + "Displays user information")
                    print("       |", Fore.CYAN + "exit :", Fore.LIGHTBLACK_EX + "Closes the terminal")
                    print("        -----------------------------------------")
                    speak("Displaying terminal instructions.")
                    chronicle_log("Displaying terminal instructions.", incognito)
                    time.sleep(2)

                elif usr == "lock":
                    chronicle_log("       <<< EMERGENCY LOCKOUT PROTOCOL INITIATED >>> ", incognito)
                    lock_protocol()

                elif usr == "incog":
                    chronicle_log("       <<< ENABLED INCOGNITO MODE >>>", incognito)
                    print(Fore.RED + "       <<< ENABLED INCOGNITO MODE >>>")
                    speak("ENABLED INCOGNITO MODE")
                    incognito = 1

                elif usr == "dis":
                    chronicle_log("       <<< DISABLED INCOGNITO MODE >>>", incognito)
                    print(Fore.GREEN + "       <<< DISABLED INCOGNITO MODE >>>")
                    speak("DISABLED INCOGNITO MODE")
                    incognito = 0

                elif usr == "clean":
                    print(Fore.GREEN + "       <<< INITIATED CLEAN SLATE PROTOCOL >>>")
                    speak("INITIATED CLEAN SLATE PROTOCOL")
                    clean_slate()
                    incognito = 1
                    print(
                        Fore.GREEN + "       All activity log files has been deleted")
                    speak("All activity log files has been deleted")

                elif usr == "reg":
                    chronicle_log("       INITIATING REGISTRATION PROTOCOL", incognito)
                    register.usr_register()

                elif usr == "profile":
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

                    chronicle_log(f"          USER PROFILE", incognito)
                    chronicle_log(f"       ● {content[0]}", incognito)
                    chronicle_log(f"       ● {content[1]}", incognito)
                    chronicle_log(f"       ● {content[2]}", incognito)
                    chronicle_log(f"       ● {content[3]}", incognito)
                    time.sleep(1)

                elif usr == "random":
                    random_scp = random.randint(1, 7100)

                    r = requests.get(f'https://scp-wiki.wikidot.com/scp-{random_scp}')
                    soup = BeautifulSoup(r.content, 'html.parser')
                    s = soup.find('div', id='page-content')
                    paras = len(s.find_all("p"))

                    print("")
                    print(Fore.YELLOW + f"     Accessing SCP-{random_scp} files")
                    speak(f"Accessing SCP-{random_scp} files")
                    chronicle_log(f"     Accessing SCP-{random_scp} files", incognito)
                    for i in range(101):
                        progress(i)
                        time.sleep(0.01)

                    print()
                    print(Fore.GREEN + "        Access granted")
                    chronicle_log("        Access granted", incognito)
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
                        print(Fore.RED + "<<< END OF FILE >>>".center(100))
                    print(Fore.RED + "<<< END OF FILE >>>".center(100))
                    print(Fore.LIGHTBLACK_EX + "File saved locally".center(100))
                    chronicle_log("<<< File saved locally >>>".center(100), incognito)
                    print("")
                    print(Fore.LIGHTBLACK_EX +
                        "Terminal developed by Ashfaaq Rifath".center(100))

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
                    chronicle_log("     Terminal output cleared", incognito)

                elif usr == "exit":
                    chronicle_log("END LOG >>>", incognito)
                    break

                else:
                    r = requests.get(f'https://scp-wiki.wikidot.com/scp-{usr}')
                    soup = BeautifulSoup(r.content, 'html.parser')
                    s = soup.find('div', id='page-content')

                    paras = len(s.find_all("p"))

                    print("")
                    print(Fore.YELLOW + f"     Accessing SCP-{usr} files")
                    speak(f"Accessing SCP-{usr} files")
                    chronicle_log(f"     Accessing SCP-{usr} files", incognito)
                    for i in range(101):
                        progress(i)
                        time.sleep(0.01)

                    print()
                    print(Fore.GREEN + "        Access granted")
                    chronicle_log("        Access granted", incognito)
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
                        print(Fore.RED + "<<< END OF FILE >>>".center(100))
                    print(Fore.RED + "<<< END OF FILE >>>".center(100))
                    print(Fore.LIGHTBLACK_EX + "File saved locally".center(100))
                    chronicle_log("<<< File saved locally >>>".center(100), incognito)
                    print("")
                    print(Fore.LIGHTBLACK_EX +
                        "Terminal developed by Ashfaaq Rifath".center(100))

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

                    speak(f"Item number : SCP-{usr}")

                    sis = s.find_all('p')[2].text
                    speak(sis)

                    lines = s.find_all('p')[3]
                    speak(lines)

    else:
        print("")
        print("      ", Fore.BLACK + Back.RED + " ACCESS DENIED ")
        speak("Access Denied")
        print("")
        print(Fore.RED + "       UNAUTHORIZED ACCESS DETECTED")
        print(Fore.RED + "       --------------------------------")
        print(Fore.RED + "       INITIATING TERMINATION PROTOCOL")
        print(Fore.RED + "       --------------------------------")
        speak("INITIATING TERMINATION PROTOCOL")

else:
        print("")
        print("      ", Fore.BLACK + Back.RED + " ACCESS DENIED ")
        speak("Access Denied")
        print("")
        print(Fore.RED + "       UNAUTHORIZED ACCESS DETECTED")
        print(Fore.RED + "       --------------------------------")
        print(Fore.RED + "       INITIATING TERMINATION PROTOCOL")
        print(Fore.RED + "       --------------------------------")
        speak("INITIATING TERMINATION PROTOCOL")



# <<< Copyright (c) 2023 Ashfaaq Rifath - SCP Foundation Terminal v2.1.3 >>>