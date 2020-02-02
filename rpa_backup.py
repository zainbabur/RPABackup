import os
from datetime import datetime, timedelta
import time

files_folder = "C:\\Users\\Zain Babur\\Documents\\"
bat_folder = "D:\\"

def check_files(filepath, batpath, delta = 2, waittime = 180):
    mtime = os.path.getmtime(filepath)
    dif = datetime.now().replace(microsecond=0)-datetime.fromtimestamp(mtime).replace(microsecond=0)
    dif_hour = dif.seconds/3600
    while dif_hour > delta:
        os.system(batpath)
        time.sleep(waittime)
        mtime = os.path.getmtime(filepath)
        dif = datetime.now().replace(microsecond=0)-datetime.fromtimestamp(mtime).replace(microsecond=0)
        dif_hour = dif.seconds/3600

check_files(filepath = files_folder+"DailyProgress.xlsx", batpath = bat_folder+"ProgressRPA.bat")
check_files(filepath = files_folder+"PlannedActivities.xlsx", batpath = bat_folder+"PlanRPA.bat", waittime=240)
check_files(filepath = files_folder+"AccessIssues.xlsx", batpath = bat_folder+"IssuesRPA.bat", delta=1)

