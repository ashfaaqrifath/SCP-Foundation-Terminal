import requests
import time
import pyttsx3
from bs4 import BeautifulSoup


def speak(talk):
    engine = pyttsx3.init("sapi5")
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(talk)
    engine.runAndWait()


usr = input("Enter SCP item number: ")

r = requests.get(f'https://scp-wiki.wikidot.com/scp-{usr}')
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('div', id='page-content')

paras = len(s.find_all("p"))

print(soup.title.text.center(100))
print("")

paras_num = range(1, paras)
num_list = list(paras_num)

bro = f"{s.find_all('p')[0].text}\n"
print(bro.center(100))

try:
    for i in num_list:
        yo = f"{s.find_all('p')[i].text}\n"
        print(yo.center(100))
except IndexError:
    print("END OF LOG")

lines = s.find_all('p')[3]
speak(f"SCP-{usr}")
speak(lines)


time.sleep(1200)