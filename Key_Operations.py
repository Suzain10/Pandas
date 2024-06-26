# -*- coding: utf-8 -*-
"""KeyOperations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Iu17PABWKNE3Jea93DSscw95m7WeTNRL
"""

import pandas as pd
df = pd.read_csv('smaller_table.csv')
df

df = pd.read_excel('/content/smaller_table _ex.xlsx')
df

df.to_csv('new_index.csv')

df.to_csv('new_noIndex.csv',index =False)

df.to_excel('new.xlsx',sheet_name ='smaller_table')

import pandas as pd
df = pd.read_csv('weather_data.csv')
df

import pandas as pd
g = df.groupby('City')
g

for City,City_df in g:
  print(City)
  print(City_df)

g.get_group('NYC')

print(g.max())

print(g.mean())

print(g.describe())

import pandas as pd
india_weather = pd.DataFrame({
    "city" : ['Pune','Agra','Sikkim'],
    'Temperature':[32,45,28],
    'Humidity':[80,60,78]

})
india_weather

import pandas as pd
US_weather = pd.DataFrame({
    "city" : ['NYC','Chicago','Orlando'],
    'Temperature':[36,25,58],
    'Humidity':[89,80,65]

})
US_weather

import pandas as pd
df = pd.concat([india_weather,US_weather])
df

import pandas as pd
df = pd.concat([india_weather,US_weather],ignore_index = True)
df

import pandas as pd
df = pd.concat([india_weather,US_weather],axis =1 )
df

temperature_df = pd.DataFrame({
    "city" : ['Pune','Agra','Sikkim','Goa'],
    'Temperature':[32,45,28,23],
})
temperature_df

humidity_df = pd.DataFrame({
    "city" : ['Pune','Agra','Sikkim'],
    'Humidity':[32,45,28],
})
humidity_df

df = pd.merge(temperature_df,humidity_df,on="city")
df

df = pd.merge(temperature_df,humidity_df,on="city",how ='outer')
df

import pandas as pd
df = pd.DataFrame([1,2,3,4,5,41,7,8,16,11],index =[49,15,13,10,178,78,56,3,28,12])
df

df.loc[15:3]

df.iloc[2]

df.iloc[2:8]

