#Hämtar filer från webben och unzippar dom

import os 
import urllib.request as urllib2
import urllib
import zipfile

path=r'C:\Users\awestroth\Privat\Fondinnehav_github\download_files_new'


os.chdir(r'C:\Users\awestroth\Privat\Fondinnehav_github\download_files_new')
response = urllib2.urlopen("https://www.fi.se/sv/vara-register/fondinnehav-per-kvartal/")
print(response.info())
html = response.read()
response.close()
print(html)

start = "https://www.fi.se"

end = []

text = str(html)

x = text.split('"')

for s in x:
    if s.endswith(".zip"):
        
        end.append(s)
        
full = []
for u in end:
    full.append(start+u)


for x in full:
    filnamn = x[x.index("filnamn=Fondinnehav_") +len("filnamn=Fondinnehav_"):x.index("filnamn=Fondinnehav_") +len("filnamn=Fondinnehav_")+6]
    x.replace(" ","")
    urllib.request.urlretrieve(x.replace(" ","%20"), filnamn+".zip")
    
    file_path = path + "\\" + filnamn + ".zip"
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(path+"\\"+filnamn)
        
        
#Lägg till if redan finns..
#Bara ladda ner den nya 
#Schedule varje kvartal? 