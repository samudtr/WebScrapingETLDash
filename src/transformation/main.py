import pandas as pd
import sqlite3
from datetime import datetime



## LEITURA DOS DADOS NO JSON
df = pd.read_json('C:/Users/samud/Documents/Python_Learning/Scrapping/data/data.jsonl', lines=True) 

pd.options.display.max_columns= None



## Novas colunas 

df['_source'] = 'meli'
df['_data_coleta'] = datetime.now()



#print(df)

#Json interpreta tudo como string, por isso, transformaremos algumas colunas em float.

df['year'] = df['year'].fillna(0)
df['km'] = df['km'].str.replace('Km', '')
df['km'] = df['km'].astype(float)




print(df)
