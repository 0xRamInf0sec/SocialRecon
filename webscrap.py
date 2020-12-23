import requests
from bs4 import BeautifulSoup


def Links():
    url=input("Enter the URL >> ")
    print('')
    print("[+] Fetching links.....")
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    for link in soup.find_all('a'):
        lin=link.get('href')
        if(lin.startswith('http')):
            print("[+] ",lin)
    print("Fetched Successfully...")
    
if __name__=="__main__":
    Links()