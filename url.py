import requests
BOLD = '\033[1m'
def urlinfo():
    inurl=input("URL >> ")
    print('')
    print('url >> '+inurl)
    url = 'https://www.virustotal.com/vtapi/v2/url/scan'
    params = {'apikey': 'APIKEY', 'url':inurl}
    response = requests.post(url, data=params)
    dictres=response.json()
    print('')
    scanid=dictres['scan_id']
    print("[+] Checking URl......")
    scanurl = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {'apikey': 'API-KEY', 'resource': scanid }
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
