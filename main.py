import datetime
import os
import random
import re
import shutil
import time

import colorama
import requests
from bs4 import BeautifulSoup
from colorama import Back, Fore
from questionary import Style as MenuStyle, select

import register
import scp001
from chronicle_engine import chronicle_log, clean_slate
from lockout import lock_protocol
from speech_engine import speak

colorama.init(autoreset=True)

APP_VERSION = "v2.2.1"
SCP_FOLDER = "SCP object files"
USER_FOLDER = "Users"
HTTP_TIMEOUT = 15
REQUEST_HEADERS = {
    "User-Agent": (
        "SCP-Foundation-Terminal/2.2 "
        "(https://github.com/ashfaaqrifath/SCP-Foundation-Terminal)"
    )
}
MENU_STYLES = MenuStyle(
    [
        ("pointer", "fg:#00FF00"),
        ("selected", "fg:#00FF00"),
        ("highlighted", "fg:#00FF00 bold"),
        ("answer", "fg:#c19c00"),
    ]
)
COMMAND_MENU = {
    "(1) SCP item lookup": "scp",
    "(2) Random SCP": "random",
    "(3) Delete SCP files": "del",
    "(4) Emergency lockout": "lock",
    "(5) Enable incognito mode": "incog",
    "(6) Disable incognito mode": "dis",
    "(7) Delete activity logs": "clean",
    "(8) Display profile": "profile",
    "(9) Clear terminal": "clear",
    "(10) Exit": "exit",
}


def ensure_directories():
    os.makedirs(SCP_FOLDER, exist_ok=True)
    os.makedirs(USER_FOLDER, exist_ok=True)


def progress(percent=0, width=30):
    symbol = width * percent // 100
    blanks = width - symbol
    print(
        "\r[ ",
        Fore.GREEN + symbol * "█",
        blanks * " ",
        " ]",
        f" {percent:.0f}%",
        sep="",
        end="",
        flush=True,
    )


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def format_item_number(item_num):
    item_int = int(item_num)
    if item_int < 1000:
        return f"{item_int:03d}"
    return str(item_int)


def format_paragraph(paragraph, length=80, left=4, right=5):
    words = paragraph.split()
    lines = []
    curline = "         " * (left - 1)

    while words:
        word = words.pop(0)
        if len(curline) + 1 + len(word) > length - right:
            lines.append(curline)
            curline = "         " * (left - 1)
        curline += " " + word

    lines.append(curline)
    return "\n".join(lines)


def parse_scp_command(command):
    match = re.search(r"\d+", command)
    if not match:
        return None
    return format_item_number(match.group())


def fetch_scp_entry(item_num):
    url = f"https://scp-wiki.wikidot.com/scp-{item_num}"
    response = requests.get(url, headers=REQUEST_HEADERS, timeout=HTTP_TIMEOUT)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    page_content = soup.find("div", id="page-content")
    if page_content is None:
        raise ValueError(f"SCP-{item_num} page content could not be found.")

    paragraphs = [p.get_text(" ", strip=True) for p in page_content.find_all("p")]
    paragraphs = [p for p in paragraphs if p]
    if not paragraphs:
        raise ValueError(f"SCP-{item_num} does not contain readable paragraphs.")

    title = soup.title.get_text(" ", strip=True) if soup.title else f"SCP-{item_num}"
    return title, paragraphs


def print_scp_entry(item_num, title, paragraphs, mode):
    print("")
    print(Fore.YELLOW + f"     Accessing SCP-{item_num} files")
    speak(f"Accessing SCP-{item_num} files")
    chronicle_log(f"     Accessing SCP-{item_num} files", mode)

    for i in range(101):
        progress(i)
        time.sleep(0.0001)

    print()
    print(Fore.GREEN + "        Access granted")
    chronicle_log("        Access granted", mode)
    print("")
    print(Fore.GREEN + title.center(100))
    print("")

    print(Fore.YELLOW + f"{paragraphs[0]}\n".center(100))
    for paragraph in paragraphs[1:]:
        print(format_paragraph(paragraph))
        print("")

    print(Fore.RED + "<< END OF FILE >>".center(100))
    print(Fore.LIGHTBLACK_EX + "File saved locally".center(100))
    chronicle_log("<< File saved locally >>".center(100), mode)
    print("")


def save_scp_entry(item_num, paragraphs):
    ensure_directories()
    save_path = os.path.join(SCP_FOLDER, f"SCP-{item_num}.txt")
    timestamp = datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")
    header = (
        f"SCP Foundation Terminal {APP_VERSION}\n"
        f"{timestamp}\n"
        "<< PROPERTY OF THE SCP FOUNDATION >>\n"
        f"SCP-{item_num} File >>\n\n"
    )

    with open(save_path, "w", encoding="utf-8") as file:
        file.write(header)
        for paragraph in paragraphs[1:]:
            file.write(format_paragraph(paragraph))
            file.write("\n\n")
        file.write("<< END OF FILE >>".center(100))
        file.write("\n")
        file.write(
            f"Copyright (c) 2026 Ashfaaq Rifath - SCP Foundation Terminal {APP_VERSION}".center(
                100
            )
        )
        file.write("\n")


def find_object_class(paragraphs):
    for paragraph in paragraphs:
        clean = paragraph.replace("\xa0", " ").strip()
        if clean.lower().startswith("object class:"):
            return clean
    return None


def speak_entry_summary(item_num, paragraphs):
    speak(f"Item number: SCP-{item_num}")
    object_class = find_object_class(paragraphs)
    if object_class:
        speak(object_class)


def show_scp_entry(item_num, mode):
    if item_num == "001":
        chronicle_log("<< ACCESS RESTRICTED >>", mode)
        chronicle_log(
            "ACCESS TO SCP-001 IS RESTRICTED TO O5 COUNCIL MEMBERS ONLY.", mode
        )
        scp001.restricted()
        return

    try:
        title, paragraphs = fetch_scp_entry(item_num)
    except (requests.RequestException, ValueError) as error:
        print("")
        print(Fore.RED + f"       Could not retrieve SCP-{item_num}: {error}")
        speak(f"Could not retrieve SCP-{item_num}")
        chronicle_log(f"       Could not retrieve SCP-{item_num}: {error}", mode)
        return

    print_scp_entry(item_num, title, paragraphs, mode)
    save_scp_entry(item_num, paragraphs)
    speak_entry_summary(item_num, paragraphs)


def show_profile(login_name, mode):
    if not login_name or login_name == "override":
        print(Fore.RED + "       User data not found")
        speak("User data not found")
        return

    try:
        with open(os.path.join(USER_FOLDER, f"{login_name}.txt"), encoding="utf-8") as user_file:
            content = user_file.readlines()
    except FileNotFoundError:
        print(Fore.RED + "       User data not found")
        speak("User data not found")
        return

    print("")
    print(Fore.CYAN + "          --------------")
    print(Fore.YELLOW + "          USER PROFILE")
    print(Fore.CYAN + "          --------------")

    for line in content[:4]:
        print("       * ", Fore.CYAN + line, end="")
        speak(line)
        chronicle_log(f"       * {line}", mode)

    chronicle_log("          USER PROFILE", mode)
    time.sleep(1)


def select_terminal_command():
    selected = select(
        "Select terminal command:",
        choices=list(COMMAND_MENU.keys()),
        qmark="",
        style=MENU_STYLES,
    ).ask()

    if selected is None:
        return "exit", "exit"

    command = COMMAND_MENU[selected]
    if command == "scp":
        item_num = input(Fore.CYAN + "       Enter SCP item number: ")
        command = f"scp-{item_num.strip()}"

    return selected, command


def command_engine(mode, login_name=None):
    ensure_directories()

    while True:
        print("")
        speak("Enter terminal command")
        chronicle_log("       Enter terminal command: ", mode)
        usr, command = select_terminal_command()
        command = command.lower()
        chronicle_log(usr, mode)

        if command.startswith("scp"):
            item_num = parse_scp_command(command)
            if item_num is None:
                print("")
                print("      ", Fore.BLACK + Back.RED + " INVALID COMMAND ")
                print(Fore.RED + "       PLEASE TRY AGAIN")
                speak("please try again")
                continue
            show_scp_entry(item_num, mode)

        elif command == "random":
            random_scp = format_item_number(str(random.randint(1, 7100)))
            show_scp_entry(random_scp, mode)

        elif command == "del":
            print(Fore.RED + "       << INITIATED PURGE PROTOCOL >>")
            speak("INITIATED PURGE PROTOCOL")
            shutil.rmtree(SCP_FOLDER, ignore_errors=True)
            ensure_directories()
            time.sleep(1)
            print(Fore.GREEN + "       All SCP object files have been deleted.")
            speak("All SCP object files have been deleted")
            chronicle_log("       INITIATED PURGE PROTOCOL", mode)
            chronicle_log("       All SCP object files have been deleted.", mode)

        elif command == "lock":
            chronicle_log("       << EMERGENCY LOCKOUT PROTOCOL INITIATED >> ", mode)
            lock_protocol()

        elif command == "incog":
            chronicle_log("       << ENABLED INCOGNITO MODE >>", mode)
            print(Fore.RED + "       << ENABLED INCOGNITO MODE >>")
            speak("ENABLED INCOGNITO MODE")
            mode = 1

        elif command == "dis":
            chronicle_log("       << DISABLED INCOGNITO MODE >>", mode)
            print(Fore.GREEN + "       << DISABLED INCOGNITO MODE >>")
            speak("DISABLED INCOGNITO MODE")
            mode = 0

        elif command == "clean":
            print(Fore.RED + "       << INITIATED PURGE PROTOCOL >>")
            speak("INITIATED PURGE PROTOCOL")
            clean_slate()
            print(Fore.GREEN + "       All activity log files have been deleted")
            speak("All activity log files have been deleted")

        elif command == "profile":
            show_profile(login_name, mode)

        elif command == "clear":
            clear_terminal()
            speak("terminal output cleared")
            chronicle_log("     Terminal output cleared", mode)

        elif command == "exit":
            chronicle_log("END LOG >>", mode)
            break

        else:
            print("")
            print("      ", Fore.BLACK + Back.RED + " INVALID COMMAND ")
            print(Fore.RED + "       PLEASE TRY AGAIN")
            speak("please try again")


def print_startup():
    print("")
    print(Fore.YELLOW + "      Connecting SCP terminal")

    for i in range(101):
        progress(i)
        time.sleep(0.0001)

    print()
    print(Fore.GREEN + "           Systems online")
    print("")
    print(
        Fore.LIGHTBLACK_EX
        + f"Copyright (c) 2026 Ashfaaq Rifath - SCP Foundation Terminal {APP_VERSION}"
    )
    time.sleep(1)
    clear_terminal()


def start_activity_log(incognito):
    timestamp = datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")
    chronicle_log(
        write=(
            f"SCP Foundation Terminal {APP_VERSION}\n"
            f"{timestamp}\n"
            "<< ACTIVITY LOG >>\n"
            "BEGIN LOG >>\n"
        ),
        incog=incognito,
    )


def print_banner(speak_warning=True):
    print("")
    print('''
                 █▀▀▀█  █▀▀█  █▀▀█   █▀▀▀  █▀▀▀█  █  █  █▄  █  █▀▀▄  █▀▀█ ▀▀█▀▀ ▀█▀  █▀▀▀█  █▄  █ 
                 ▀▀▀▄▄  █     █▄▄█   █▀▀▀  █   █  █  █  █ █ █  █  █  █▄▄█   █    █   █   █  █ █ █ 
                 █▄▄▄█  █▄▄█  █      █     █▄▄▄█  █▄▄█  █  ▀█  █▄▄▀  █  █   █   ▄█▄  █▄▄▄█  █  ▀█
                                    SECURE   ●   CONTAIN   ●   PROTECT''')
    print("")
    print(
        "         ",
        Back.RED
        + " WARNING. THE SCP FOUNDATION DATABASE IS CLASSIFIED. UNAUTHORIZED ACCESS IS STRICTLY PROHIBITED ",
    )
    if speak_warning:
        speak(
            "WARNING. THE SCP FOUNDATION DATABASE IS CLASSIFIED. UNAUTHORIZED ACCESS IS STRICTLY PROHIBITED."
        )
    print("")

def get_registered_password(login_name):
    try:
        with open(os.path.join(USER_FOLDER, f"{login_name}.txt"), encoding="utf-8") as user_file:
            lines = user_file.readlines()
    except FileNotFoundError:
        return None

    if len(lines) < 5:
        return None
    return lines[4].strip()


def select_access_option():
    selected = select(
        "Select access option:",
        choices=["Login", "Register"],
        qmark="",
        style=MENU_STYLES,
    ).ask()

    return selected or "Login"


def clear_for_terminal():
    clear_terminal()
    print_banner(speak_warning=False)


def main():
    ensure_directories()
    print_startup()

    incognito = 0
    start_activity_log(incognito)
    print_banner()

    attempts = 3
    o5_code = 0

    while attempts > 0:
        access_option = select_access_option()

        if access_option == "Register":
            chronicle_log("       INITIATING REGISTRATION PROCEDURE", incognito)
            login_name = register.usr_register()
            clear_for_terminal()
            command_engine(incognito, login_name)
            break

        login_name = input("       Enter username: ").strip()
        password_ok = False
        if login_name == "override":
            chronicle_log("<< TERMINAL OVERRIDE >>", incognito)
            chronicle_log("END LOG >>", incognito)
            incognito = 1

            print(Fore.RED + "       << TERMINAL OVERRIDE >>")
            print("")
            speak("Enter security override code")
            login_pass = input(Fore.RED + "       Enter security override code: ").strip()
        else:
            login_pass = input("       Enter password: ").strip()

        print(Fore.YELLOW + "       Verifying credentials...")
        time.sleep(1.5)

        if login_name == "override":
            if login_pass != "2002":
                print("")
                print("      ", Fore.BLACK + Back.RED + " INVALID OVERRIDE CODE ")
                speak("INVALID OVERRIDE CODE")
                chronicle_log(
                    "       << EMERGENCY LOCKOUT PROTOCOL INITIATED >> ", incognito
                )
                o5_code = lock_protocol()
        else:
            stored_password = get_registered_password(login_name)
            password_ok = stored_password is not None and login_pass == stored_password

        if (login_name == "override" and login_pass == "2002") or password_ok or o5_code == 1:
            if login_name == "override" and o5_code != 1:
                print(Fore.GREEN + "       Override code accepted")
                speak("Override code accepted")

            if o5_code != 1:
                print("      ", Fore.BLACK + Back.GREEN + " ACCESS GRANTED ")
                speak("Access granted.")

                if login_name != "override":
                    print("")
                    print(Fore.GREEN + f"       Welcome {login_name}")
                    speak(f"Welcome {login_name}")
                    chronicle_log(f"       Welcome {login_name}", incognito)

            clear_for_terminal()
            command_engine(incognito, login_name)
            break

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
            clear_for_terminal()
            command_engine(incognito)


if __name__ == "__main__":
    main()
