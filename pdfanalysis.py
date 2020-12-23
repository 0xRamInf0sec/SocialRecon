from PyPDF2 import PdfFileReader

def pdfinfo():
    filep=input("File path >> ")
    with open(filep, 'rb') as f:
            pdf = PdfFileReader(f)
            info = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()
    try:
        author = info.author
        creator = info.creator
        producer = info.producer 
        print("[+] Author        : ",author)
        print("[+] Creator       : ",creator)
        print("[+] Producer      : ",producer)
        cdate=info['/CreationDate']
        cyear=cdate[2:6]
        cmonth=cdate[6:8]
        cd=cdate[8:10]
        print("[+] Creation Date : ",cd,":",cmonth,":",cyear) 
        mdate=info['/ModDate']
        myear=cdate[2:6]
        mmonth=cdate[6:8]
        md=cdate[8:10]    
        print("[+] Modified Date : ",md,":",mmonth,":",myear) 
    except:
        print("[-] Meta data not available")
if __name__=="__main__":
    pdfinfo()