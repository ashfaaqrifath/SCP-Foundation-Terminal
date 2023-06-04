import os
import sys
import time
import datetime

date = datetime.datetime.now().strftime("%h:%H:%M:%S")
act_log = str(date).replace(":", "-") + "-Log.txt"

#first of all create a folder named Activity Logs
folder = "Activity Logs"
save_path = os.path.join(folder, act_log)

def chronicle_log(write, incog):
    #enabled activity logging
    if incog == 0:
        print_save = sys.stdout
        f = open(save_path, 'a', encoding="utf-8")
        sys.stdout = f
        y = write
        print(y)
        sys.stdout = print_save
        f.close()

    #disabled activity logging
    elif incog == 1:
        print_save = sys.stdout
        f = open(save_path, 'a', encoding="utf-8")
        sys.stdout = f
        y = write
        pass
        #activity logging diabled
        sys.stdout = print_save
        f.close()

def clean_slate():
    mydir = "Activity Logs"
    txtfiles = [f for f in os.listdir(mydir) if f.endswith(".txt")]
    for f in txtfiles:
        os.remove(os.path.join(mydir, f))

    time.sleep(1)
    #deletes all activity log files in the folder