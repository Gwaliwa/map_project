import os 
from urllib.request import urlopen 

#assign url in data storage
url = "https://www.imf.org/external/datamapper/api/v1/PCPIPCH?periods=2023"
curl = "https://www.imf.org/external/datamapper/api/v1/countries"

#open urls
#save them to request
request = urlopen(url)
crequest = urlopen(curl)

#read urls
data = request.read().decode('UTF-8')
cdata = crequest.read().decode('UTF-8')

#save the urls in inflation.json
#save curl in countries.json

with open('inflation.json', 'w') as file:
    file.write(data)

with open('countries.json','w') as cfile:
    cfile.write(cdata)

#create a function
#call a function that
#convert file to csv
def freshdata():
    os.system('imf_to_csv.py')









#https://aravindkumarvemula.medium.com/retrieving-data-from-api-and-storing-in-json-file-python-4f62f1269c87



