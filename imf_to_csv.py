import json
import os


#open json files
#open inflation file
#save content is storage called jsonString
#load the json into string ie python data
with open('inflation.json','r') as file:
    jsonString = file.read()
pydata = json.loads(jsonString)


#repeat the above process
#for country.json data

with open('countries.json', 'r') as cfile:
    jcountries = cfile.read()
cpydata = json.loads(jcountries)

#extract country code 
#extract inflation 
#from inflation file
#start to read afterPCPIPCH which is after values
#csvData reads after 2023 (contains key, inflation)
values = pydata['values']['PCPIPCH']
keys = list(values.keys())
csvData = [[key, values[key]['2023']] for key in keys]

#combine csvData with countries through key(country code)

for row in csvData:
    country_code = row[0]
    country_name = ""

#check if country code incsv is in countries data(cpydata after countries)
    if country_code in cpydata['countries']:
        country_name = cpydata['countries'][country_code]['label']
    row.insert(0, f'{country_name}')

cvc = '\n'.join([','.join(map(str,row)) for row in csvData])

data_head = "country,code,inflation_rate,empty\n" + cvc

#print(data_head) 

#save data in file called inflation.cvs

with open('inflation1.csv', 'w') as file:
    file.write(data_head)

#def cleandata():
    #os.system('clean_data.py')
print("imf to csv data successiful")
