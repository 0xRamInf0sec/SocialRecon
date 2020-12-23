import requests
import pyfiglet
from halo import Halo
from gtts import gTTS  
from playsound import playsound
from bs4 import BeautifulSoup
spinner = Halo(text=' Scanning', spinner='dots')
R = '\033[31m' 
G = '\033[32m'
C = '\033[36m'
W = '\033[0m' 
def recon():
    image=input(C+"Enter the image path >> ")
    try:
        mytext = "Scanning started boss"
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("welcome.mp3") 
        playsound("welcome.mp3")       
        spinner.start()   
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
        url='http://www.google.co.in/searchbyimage/upload'
        secondurl={'encoded_image': (image, open(image, 'rb')), 'image_content': ''}
        response = requests.post(url, files=secondurl,allow_redirects=False)
        fetch=response.headers['Location']
        #print(fetch)
        req=requests.get(fetch,headers=headers)
        socialmedia=["instagram","facebook","twitter","linkedin","github"]
        linklist=[]
        print(G+"[+] Scan started......")
        print(G+"Checking whether the image is associated in any social media ")
        print(G+"Scanning started in Instagram")
        print(G+"Scanning started in Github")
        print(G+"Scanning started in Facebook")
        print(G+"Scanning started in Twitter")
        print(G+"Scanning started in Linkedin")           
        if(req.status_code == 200):
            soup = BeautifulSoup(req.content,'html.parser')
            for g in soup.find_all('div', class_='g'):
                anchors = g.find_all('a')
                if 'href' in str(anchors[0]):
                    linklist.append(anchors[0]['href'])
                    #print(linklist)
            c=0
            for i in socialmedia:
                sm=str(i)
                #print(sm)
                for j in linklist:
                    if sm in str(j):
                        c=c+1   
                        print(C+"[+]"+j)
            if c == 0:
                mytext = "No social media links found"
                language = 'en'
                myobj = gTTS(text=mytext, lang=language, slow=False) 
                myobj.save("welcome.mp3") 
                playsound("welcome.mp3")               
                print(R+"No social Media links associated with this image")
            else:
                mytext = "Social media Links found"
                language = 'en'
                myobj = gTTS(text=mytext, lang=language, slow=False) 
                myobj.save("welcome.mp3") 
                playsound("welcome.mp3")               
        spinner.stop()
    except Exception as e:
        print(e)
if __name__ == "__main__":
    recon()