import colorama
import requests
from bs4 import BeautifulSoup
import time
import pyttsx3
from colorama import Fore, Back
colorama.init(autoreset=True)


def casper_speak(talk):
    engine = pyttsx3.init("sapi5")
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(talk)
    engine.runAndWait()


def progress(percent=0, width=30):

    symbol = width * percent // 100
    blanks = width - symbol

    print('\r[ ', Fore.GREEN + symbol * "█", blanks*' ', ' ]', f' {percent:.0f}%', sep='',
          end='', flush=True)

print("")
print(Fore.YELLOW + " Connecting SCP Foundation terminal")
for i in range(101):
    progress(i)
    time.sleep(0.01)

print()
print(Fore.GREEN + "           Systems online")
print("")


print('''
                 █▀▀▀█  █▀▀█  █▀▀█   █▀▀▀  █▀▀▀█  █  █  █▄  █  █▀▀▄  █▀▀█ ▀▀█▀▀ ▀█▀  █▀▀▀█  █▄  █ 
                 ▀▀▀▄▄  █     █▄▄█   █▀▀▀  █   █  █  █  █ █ █  █  █  █▄▄█   █    █   █   █  █ █ █ 
                 █▄▄▄█  █▄▄█  █      █     █▄▄▄█  █▄▄█  █  ▀█  █▄▄▀  █  █   █   ▄█▄  █▄▄▄█  █  ▀█
                                    SECURE   ●   CONTAIN   ●   PROTECT''')
print("")
print("         ", Back.RED + " WARNING. THE SCP FOUNDATION DATABASE IS CLASSIFIED. UNAUTHORIZED PERSONAL IS STRICTLY PROHIBITED ")
# casper_speak("WARNING. THEE SCP FOUNDATION DATABASE IS CLASSIFIED. UNAUTHORIZED PERSONAL IS STRICTLY PROHIBITED.")


# dum = input("   Enter login credentials: ")

# print("Verifying credentials...")
# casper_speak("Verifying credentials")
# time.sleep(0.05)

# print("Clearance granted.")
# casper_speak("Clearance granted.")

casper_speak("Enter SCP item number.")
usr = input("   Enter SCP item number: ")

r = requests.get(f'https://scp-wiki.wikidot.com/scp-{usr}')
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('div', id='page-content')

paras = len(s.find_all("p"))

print(Fore.YELLOW + f"    Accessing SCP-{usr} documents")
for i in range(101):
    progress(i)
    time.sleep(0.01)

print()
print(Fore.BLUE + "        Access granted")
print("")

print(Fore.GREEN + soup.title.text.center(100))
print("")

paras_num = range(1, paras)
num_list = list(paras_num)

bro = f"{s.find_all('p')[0].text}\n"
print(Fore.YELLOW + bro.center(100))


try:
    for i in num_list:
        txt = f"{s.find_all('p')[i].text}"


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
            print(format_paragraph(paragraph, 80, left=4, right=5))
            print()  # next paragraph

except IndexError:
    print(Fore.RED + "<<< END OF DOCUMENT >>>".center(100))
print(Fore.RED + "<<< END OF DOCUMENT >>>".center(100))


casper_speak(f"Item number : SCP-{usr}")

sis = s.find_all('p')[2].text
casper_speak(sis)

lines = s.find_all('p')[3]
casper_speak(lines)


time.sleep(3600)
