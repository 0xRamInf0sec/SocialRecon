
from PIL import Image
from PIL.ExifTags import TAGS
from gtts import gTTS  
from playsound import playsound
from geopy.geocoders import Nominatim
import webbrowser
R = '\033[31m' 
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'
def map_it(lat, lon):
    mytext = "GPS Location FOUND!!"
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("welcome.mp3") 
    playsound("welcome.mp3")     
    print(G+'Gps Location Fouund !!')
    print("Latitude  : %s" % lat)
    print("Longitude : %s" % lon)
    print('')
    mytext = "Do you want know the place of the gps location "
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("gps.mp3") 
    playsound("gps.mp3") 
    opt=input("Enter Y or N :")
    if(opt =='Y'):
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.reverse(str(lat)+","+str(lon))
        mapurl = "https://maps.google.com/maps?q=%s,+%s" % (lat, lon)
        webbrowser.open(mapurl, new=2)        
        mytext ="Location Identified Boss !!"
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("out.mp3") 
        playsound("out.mp3")         
        print(C+"Location Found : ",location) 
        print('')
        
    else:
        mytext ="Thanks for using meta data extractor !!"
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("out.mp3") 
        playsound("out.mp3")    
        
  
def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret
def gps():
    imagename=input("Enter the filepath : " )
    exif=get_exif(imagename)
    for key,value in exif.items():
        print("%s : %s" %(key,value))
    if "GPSInfo" in exif:
        lat = [float(x) / float(y) for x, y in exif['GPSInfo'][2]]
        latref = exif['GPSInfo'][1]
        lon = [float(x) / float(y) for x, y in exif['GPSInfo'][4]]
        lonref = exif['GPSInfo'][3]
        lat = lat[0] + lat[1] / 60 + lat[2] / 3600
        lon = lon[0] + lon[1] / 60 + lon[2] / 3600
        if latref == 'S':
            lat = -lat
        if lonref == 'W':
            lon = -lon
        map_it(lat, lon)
    else:
        mytext = "GPS Location Not FOUND!!"
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("welcome.mp3") 
        playsound("welcome.mp3")        
        print('')
        print("GPS location not found")
        print('')
        
if __name__ == "__main__":
    gps()