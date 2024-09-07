import pandas as pd
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
import os 



## Json Data Reading. <dtype = str> garantees that thousands marks for numbers will not be misinterpreted
df = pd.read_json('C:/Users/samud/Documents/Python_Learning/Scrapping/data/data.jsonl', lines=True, dtype = str) 

## Option to display all columns in terminal.
pd.options.display.max_columns= None


df['year'] = df['year'].fillna(0).astype(float)

df['km'] = df['km'].str.replace(r'[Kk]m|\.','', regex=True).astype(float)

df['price'] = df['price'].str.replace('.','').astype(float)

df[['city', 'state']] = df['location'].str.split('-', expand=True)

df = df.drop(columns=['location'])

## Control Columns
df['_source'] = 'meli'
df['_data_coleta'] = datetime.now().strftime("%d/%m/%Y")
##


## SQLite Configuration - Local DBMS that does not require client-server connection

conn = sqlite3.connect('C:/Users/samud/Documents/Python_Learning/Scrapping/data/quotes.db')


## Saves into recently created DBMS

df.to_sql('meli_carros',conn,if_exists = 'replace', index = False)

## Close sqlite3 connection
conn.close()

## AWS RDS Connection: 



