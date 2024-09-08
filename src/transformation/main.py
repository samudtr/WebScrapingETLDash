import pandas as pd
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os 

#### DATAPREP #### 

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


## AWS Connection:

# Step 1: Load the environment variables from the .env file

load_dotenv()

DB_HOST = os.getenv("DB_HOST_PROD")
DB_PORT = os.getenv("DB_PORT_PROD")
DB_NAME = os.getenv("DB_NAME_PROD")
DB_USER = os.getenv("DB_USER_PROD")
DB_PASS = os.getenv("DB_PASS_PROD")
DB_SCHEMA = os.getenv("DB_SCHEMA_PROD")

# Step 2: Create the SQLAlchemy engine
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
conn = engine.connect()


# Step 4: Write the DataFrame to the PostgreSQL database

df.to_sql('cars', conn, schema=DB_SCHEMA, if_exists='replace', index=False)

conn.close()
