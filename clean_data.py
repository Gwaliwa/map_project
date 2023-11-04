import pandas as pd 
import numpy as np
import ast
import re


def myfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

df= pd.read_csv("inflation1.csv", on_bad_lines='skip', encoding='utf-8')
print(df.columns.tolist())
#res = test_string.replace('.', '', 1).isdigit() 

for index, row in df.iterrows():
    my_num = row['inflation_rate']

    x = str(myfloat(my_num))

    if x != 'True':
        df.loc[index, 'inflation_rate'] = row['empty']
        print(row['empty'])
    #else:
        #df.loc[x, 'inflation_rate'] = row['empty']
        #row['inflation_rate'] = row['empty']
        #print (row['inflation_rate'])

df.loc[2, 'country'] = 'Cape Verde'
df.loc[16, 'country'] = 'Brunei'
df.loc[43, 'country'] = 'Turkey'
df.loc[57, 'country'] = 'The Bahamas'
df.loc[58, 'country'] = 'The Gambia'
df.loc[62, 'country'] = 'United States of America'
df.loc[66, 'country'] = 'Venezuela'
df.loc[68, 'country'] = 'Yemen'
df.loc[69, 'country'] = 'Slovakia'
df.loc[76, 'country'] = 'Taiwan'
df.loc[122, 'country'] = 'Micronesia'
df.loc[133, 'country'] = 'North Korea'
df.loc[163, 'country'] = 'Hong Kong'
df.loc[137, 'country'] = 'Macau'
df.loc[167, 'country'] = 'Iran'
df.loc[174, 'country'] = 'Laos'
df.loc[187, 'country'] = 'Czechia'
df.loc[191, 'country'] = 'Egypt'
df.loc[187, 'country'] = 'Czechia'


print(df.to_string())

df.to_csv('inflation.csv', encoding='utf-8', index=False)
