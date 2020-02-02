import os
from datetime import datetime, timedelta
import time


files_folder = "C:\\Users\\Zain Babur\\Documents\\"
bat_folder = "D:\\"

def check_files(filepath, batpath, delta = 2, waittime = 180):
    mtime = os.path.getmtime(filepath) #get modified time of the file
    dif = datetime.now().replace(microsecond=0)-datetime.fromtimestamp(mtime).replace(microsecond=0) #calculate difference of modified time from now
    dif_hour = dif.seconds/3600 #get number of hours passed
    while dif_hour > delta: #until file is updated, keep running the batch file
        os.system(batpath) #run batch file
        time.sleep(waittime) #python waits for the RPA to finish running but we still need to wait for the file to be updated, which is done through other python scripts
        mtime = os.path.getmtime(filepath) #get modified time again
        dif = datetime.now().replace(microsecond=0)-datetime.fromtimestamp(mtime).replace(microsecond=0) #get difference
        dif_hour = dif.seconds/3600 

#do this process for multiple files
check_files(filepath = files_folder+"DailyProgress.xlsx", batpath = bat_folder+"ProgressRPA.bat")
check_files(filepath = files_folder+"PlannedActivities.xlsx", batpath = bat_folder+"PlanRPA.bat", waittime=240)
check_files(filepath = files_folder+"AccessIssues.xlsx", batpath = bat_folder+"IssuesRPA.bat", delta=1)

