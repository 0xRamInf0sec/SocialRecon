import requests
import webbrowser
from gtts import gTTS  
from playsound import playsound

R = '\033[31m' 
G = '\033[32m'
C = '\033[36m'
W = '\033[0m' 

def iplocate():
    ipinfo={}
    ip=input("Ip address >> ")
    url="http://ip-api.com/json/"+ip
    r=requests.get(url)
    ipinfo=r.json()
    if ipinfo['status'] == 'success':
        lat=ipinfo['lat']
        lon=ipinfo['lon']        
        print(G+"Ip location Found !!")
        mytext = "IP location Found !!"
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("found.mp3") 
        playsound("found.mp3") 
        print('Country     : ',ipinfo['country'])
        print('Region Name : ',ipinfo['regionName'])
        print('City        : ',ipinfo['city'])
        print('Time zone   : ',ipinfo['timezone'])
        print('ISP         : ',ipinfo['isp'])
        print(C+'Opening Location in browser')
        mapurl = "https://maps.google.com/maps?q=%s,+%s" % (lat, lon)
        webbrowser.open(mapurl, new=2) 
        print('')
    else:
        print(R+"Ip location Not Found !!")
        mytext = "IP location not Found !!"
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("found.mp3") 
        playsound("found.mp3") 
        print('')
        
if __name__=="__main__":
    iplocate()
