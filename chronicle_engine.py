import datetime
import os
import time

LOG_FOLDER = "Activity Logs"

os.makedirs(LOG_FOLDER, exist_ok=True)

date = datetime.datetime.now().strftime("%b-%H-%M-%S")
act_log = f"{date}-Log.txt"
save_path = os.path.join(LOG_FOLDER, act_log)


def chronicle_log(write, incog):
    if incog == 1:
        return

    with open(save_path, "a", encoding="utf-8") as file:
        print(write, file=file)


def clean_slate():
    os.makedirs(LOG_FOLDER, exist_ok=True)
    txtfiles = [f for f in os.listdir(LOG_FOLDER) if f.endswith(".txt")]
    for file_name in txtfiles:
        os.remove(os.path.join(LOG_FOLDER, file_name))

    time.sleep(1)
