import requests
from gtts import gTTS  
from playsound import playsound
R = '\033[31m' 
G = '\033[32m'
C = '\033[36m'
W = '\033[0m' 
def email():
    dictemail={}
    email=input("Email address to check >> ")
    url="https://app.verify-email.org/api/v1/mFyMW4NCYyyI8mRcK3mIzkIYNu1BnWskMNPabWyOJU007FVH1I/verify/"+email
    r=requests.get(url)
    dictemail=r.json()
    print("Email     : ",dictemail.get('email'))
    print("smtp code : ",dictemail.get('smtp_code'))
    stat=dictemail.get('smtp_log')
    language='en'
    if(stat == 'Success'):
        text="Email address found "
        aud=gTTS(text=text,lang=language,slow=False)
        aud.save("valid.mp3")
        playsound("valid.mp3")
        print(G+"Status     : "+stat)
    else:
        text="Email address not found "
        aud=gTTS(text=text,lang=language,slow=False)
        aud.save("valid.mp3")
        playsound("valid.mp3")            
        print(R+"Status     : "+stat)
if __name__=="__main__":
    email()