
## Required resources for this stage
import streamlit as st
import pandas as pd
import sqlite3



## Connect to SQL Database
conn = sqlite3.connect('C:/Users/samud/Documents/Python_Learning/Scrapping/data/quotes.db')


## Make a query using pandas to retrieve data and store it to a df
df = pd.read_sql_query("SELECT * FROM meli_carros", con=conn)


## Close DB connection
conn.close()


## Streamlit

#App title

st.title('Pesquisa Aberta de Carros no Meli')

## Print sample table
st.write(df.head(40))


# Main KPIs

st.subheader("KPIs Veículos")

# Division in 3 columns

c1,c2,c3 = st.columns(3)

total_cars = df.shape[0]

#columns
c1.metric(label = 'Sample Size',value = total_cars)


## Proportion of cars per state

## Mean KM cars per state

## Avg year cars per state






