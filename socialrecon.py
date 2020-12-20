import pyfiglet
from gtts import gTTS  
from playsound import playsound
import time
import sys
from imagerecon import recon
from exif import gps
from emailverify import email
from username import username
R = '\033[31m' 
G = '\033[32m'
C = '\033[36m'
W = '\033[0m' 
ban=pyfiglet.figlet_format("Social Recon",font="slant")
print(ban)
string="Tool created by - Ramalingasamy M K"
for char in string:
    print(char,end='')
    sys.stdout.flush()
    time.sleep(0.1)
print()
mytext = "Welcome to Social reconnaissance"
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
playsound("welcome.mp3") 
print('')
print(C+"""Tools available 
        1.Meta data extraction
        2.Image recon
        3.Email verifier
        4.Username Finder
        """)
text="Can you Select any tool sir? "
aud=gTTS(text=text,lang=language,slow=False)
aud.save("options.mp3")
playsound("options.mp3")
inp=int(input("Enter the option : "))
if(inp == 1):
    gps()
elif(inp == 2):
    recon()
elif(inp==3):
    email()
elif(inp==4):
    username()
else:
    text="please enter an valid option "
    aud=gTTS(text=text,lang=language,slow=False)
    aud.save("valid.mp3")
    playsound("valid.mp3")    