
## Required resources for this stage
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os 




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

## Make a query using pandas to retrieve data and store it to a df
df = pd.read_sql_query("SELECT * FROM cars", con=conn)


## Close DB connection
conn.close()


## Streamlit

#App title

st.title('Open Dashboard for Cars Marketplace in Brazil')

# General Information

st.subheader("General Information")

# Division in 3 columns

c1,c2,c3 = st.columns(3)

total_cars = df.shape[0]



# KPI 1: Total Cars
total_cars = df.shape[0]
c1.metric(label='Sample Size', value=total_cars)

# KPI 2: Average Price of Cars
avg_price = df['price'].mean()
c2.metric(label='Average Price', value=f"R$ {avg_price:,.2f}")

# KPI 3: Average Year of Cars
avg_year = df['year'].mean()
c3.metric(label='Average Year', value=f"{avg_year:.0f}")

## Other 3 columns

c4,c5,c6 = st.columns(3)

# KPI 3: Min Year of Cars
min_year = df['year'].min()
c4.metric(label='Min Year', value=f"{min_year:.0f}")

# KPI 4: Average Kilometers of Cars
avg_km = df['km'].mean()
c5.metric(label='Average Kilometers', value=f"{avg_km:,.0f} Km")

# KPI 5: Collection Date
collect_date = df['_data_coleta'].max()
c6.metric(label='Updated', value=collect_date)

# Proportion of Cars by State
st.subheader("Proporção de Carros por Estado")
state_counts = df['state'].value_counts(normalize=True) * 100
st.bar_chart(state_counts)

# Mean Kilometers by State
st.subheader("Média de KM por Estado")
mean_km_by_state = df.groupby('state')['km'].mean()
st.bar_chart(mean_km_by_state)

# Average Year of Cars by State
st.subheader("Média de Ano de Carros por Estado")
avg_year_by_state = df.groupby('state')['year'].mean()
st.bar_chart(avg_year_by_state)

# Filter by State
st.subheader("Filtrar por Estado")
state_filter = st.selectbox("Escolha um Estado", df['state'].unique(), index=0)

# Filter the data based on selected state
filtered_df = df[df['state'] == state_filter]

# Line Chart: Average Price of Cars by Year for Selected State
st.subheader(f"Preço Médio de Carros por Ano no Estado {state_filter}")
avg_price_by_year = filtered_df.groupby('year')['price'].mean()

# Plot the line chart using Streamlit
st.line_chart(avg_price_by_year)
