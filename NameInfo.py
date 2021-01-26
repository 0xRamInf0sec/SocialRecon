import requests
import webbrowser
from bs4 import BeautifulSoup
R = '\033[31m' 
G = '\033[32m'
C = '\033[36m'
W = '\033[0m' 
def Nameinfo():
    name=input("Enter the Full Name  >> ")
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }   
    try:
        url="https://www.google.com/search?q="+name
        response=requests.get(url,headers=headers)
        socialmedia=["instagram","facebook","twitter","linkedin","github","scholar","hackerearth","hackerrank","hackerone","tiktok","youtube","books","researchgate","publons","orcid","maps"]
        linklist=[]        
        soup=BeautifulSoup(response.content,'html.parser')
        for g in soup.find_all('div', class_='g'):
            anchors = g.find_all('a')
            if 'href' in str(anchors[0]):
                linklist.append(anchors[0]['href'])
        c=0
        foundedlinks=[]
        for i in socialmedia:
            sm=str(i)
                    #print(sm)
            for j in linklist:
                if sm in str(j):
                    c=c+1
                    foundedlinks.append(j)
                    print(C+"[+]"+j)
        #print(foundedlinks)
        for i in foundedlinks:
            webbrowser.open(i)
        print(R+"[-] Checking for any pdf documents associated with this name .....")
        url="https://www.google.com/search?q=%22"+name+"%22+filetype%3Apdf&oq=%22"+name+"%22+filetype%3Apdf"
        response=requests.get(url,headers=headers)
        soup=BeautifulSoup(response.content,'html.parser')
        f=0
        for g in soup.find_all('div', class_='g'):
            links = g.find_all('a')
            if 'href' in str(links[0]):
                print(G+"[+]"+links[0]['href'])
        if c == 0:              
            print(R+"No Info about this person")        
    except Exception as e:
        print(e)
        


if __name__=="__main__":
    Nameinfo()