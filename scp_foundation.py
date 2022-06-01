import colorama
import requests
from bs4 import BeautifulSoup
import time
import pyttsx3
from colorama import Fore, Back
colorama.init(autoreset=True)


def speak(talk):
    engine = pyttsx3.init("sapi5")
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(talk)
    engine.runAndWait()


print('''
                 █▀▀▀█  █▀▀█  █▀▀█   █▀▀▀  █▀▀▀█  █  █  █▄  █  █▀▀▄  █▀▀█ ▀▀█▀▀ ▀█▀  █▀▀▀█  █▄  █ 
                 ▀▀▀▄▄  █     █▄▄█   █▀▀▀  █   █  █  █  █ █ █  █  █  █▄▄█   █    █   █   █  █ █ █ 
                 █▄▄▄█  █▄▄█  █      █     █▄▄▄█  █▄▄█  █  ▀█  █▄▄▀  █  █   █   ▄█▄  █▄▄▄█  █  ▀█
                                    SECURE   ●   CONTAIN   ●   PROTECT''')


usr = input("Enter SCP item number: ")

r = requests.get(f'https://scp-wiki.wikidot.com/scp-{usr}')
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('div', id='page-content')

paras = len(s.find_all("p"))

print(Fore.GREEN + soup.title.text.center(100))
print("")

paras_num = range(1, paras)
num_list = list(paras_num)

bro = f"{s.find_all('p')[0].text}\n"
print(Fore.YELLOW + bro.center(100))

try:
    for i in num_list:
        yo = f"{s.find_all('p')[i].text}\n"
        print(Fore.GREEN + yo.center(100))
except IndexError:
    print(Fore.RED + "<<< END OF DOCUMENT >>>".center(100))
print(Fore.RED + "<<< END OF DOCUMENT >>>".center(100))


speak(f"Item number : SCP-{usr}")

sis = s.find_all('p')[2].text
speak(sis)

lines = s.find_all('p')[3]
speak(lines)


time.sleep(1200)
