import pyfiglet
from gtts import gTTS  
from playsound import playsound
import time
import sys
from url import urlinfo
from pdfanalysis import pdfinfo
from imagerecon import recon
from exif import gps
from emailverify import email
from username import username
from iplocator import iplocate
from Instagraminfo import instainfo
from webscrap import Links
from NameInfo import Nameinfo
R = '\033[31m' 
G = '\033[32m'
C = '\033[36m'
W = '\033[0m' 

def reconinput():
    inp=(input("social recon >> "))
    if(inp == '1'):
        gps()
    elif(inp == '2'):
        recon()
    elif(inp=='3'):
        email()
    elif(inp=='4'):
        username()
    elif (inp=='5'):
        iplocate()
    elif(inp=='6'):
        instainfo()
    elif(inp =='7'):
        urlinfo()
    elif (inp=='8'):
        pdfinfo()
    elif(inp=='9'):
        Links()
    elif (inp=='10'):
        Nameinfo()
    elif(inp=='exit'):
        exit()
    else:
        text="please enter an valid option "
        aud=gTTS(text=text,lang=language,slow=False)
        aud.save("valid.mp3")
        playsound("valid.mp3")   
        
if __name__=="__main__":
    print(
            """ 
                     
     _____            _       _  ______                     
    /  ___|          (_)     | | | ___ \                    
    \ `--.  ___   ___ _  __ _| | | |_/ /___  ___ ___  _ __  
     `--. \/ _ \ / __| |/ _` | | |    // _ \/ __/ _ \| '_ \ 
    /\__/ | (_) | (__| | (_| | | | |\ |  __| (_| (_) | | | |
    \____/ \___/ \___|_|\__,_|_| \_| \_\___|\___\___/|_| |_|
           
            """
        )
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
    
            1.Image Meta data extraction
            2.Social media hunting using image
            3.Email verifier
            4.Username Finder
            5.IP location Lookup
            6.Instagram Info lookup
            7.URL lookup
            8.PDF meta data analysis
            9.URL lookup in webpages
            10.Information Gathering using Name
            usage : type exit to stop
            """)
    print('')
    
    text="Can you Select any tool sir? "
    aud=gTTS(text=text,lang=language,slow=False)
    aud.save("options.mp3")
    playsound("options.mp3")   
    while True:
        reconinput()
