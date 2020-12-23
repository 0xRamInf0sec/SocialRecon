from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from halo import Halo
from gtts import gTTS  
from playsound import playsound

R = '\033[31m' 
G = '\033[32m'
C = '\033[36m'
W = '\033[0m' 

def username():
    name=input("Enter the username : ")
    spinner = Halo(text=' Username Scanning started', spinner='dots')
    spinner.start()
    mytext = "Username scanning started !!"
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("welcome.mp3") 
    playsound("welcome.mp3")     
    op = webdriver.ChromeOptions()
    op.add_argument('headless')  
    driver=webdriver.Chrome(options=op,executable_path="/home/ram/Desktop/chromedriver")
    driver.get("https://instantusername.com/#/")
    time.sleep(3)
    driver.find_element_by_xpath("//input[@class='ant-input ant-input-lg']").send_keys(name)
    time.sleep(6)
    page=driver.page_source
    soup=BeautifulSoup(page,'html.parser')
    spinner.stop()
    c=0
    for link in soup.find_all('a',class_='card available'):
        c=c+1
        print(C+"[+]"+link['href'])
    if(c==0):
        print(R+"No social media accounts associated with this username")
    print('')
if __name__=="__main__":
    username()