import requests
BOLD = '\033[1m'
def urlinfo():
    inurl=input("URL >> ")
    print('')
    print('url >> '+inurl)
    url = 'https://www.virustotal.com/vtapi/v2/url/scan'
    params = {'apikey': '28fadf8f17d413060698031cee5ce3d53cae7be223fe01c11b0203af922b941e', 'url':inurl}
    response = requests.post(url, data=params)
    dictres=response.json()
    print('')
    scanid=dictres['scan_id']
    print("[+] Checking URl......")
    scanurl = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {'apikey': '28fadf8f17d413060698031cee5ce3d53cae7be223fe01c11b0203af922b941e', 'resource': scanid }
    response = requests.get(scanurl, params=params)
    dictreport=response.json()
    print('Total Scanning >> ',dictreport['total'])
    sites=dictreport['scans'] 
    for x in sites:
        print(BOLD+x)
        #print(sites[x])
        for y in sites[x]:
            print("       ",y," : ",sites[x][y])
            

if __name__=="__main__":
    urlinfo()