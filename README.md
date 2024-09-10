# Webscraping + AWS RDS + Dashboard App project

This project showcases my skills to build a webscraping robot **(Scrapy)**, transform the data **(Pandas)**, store it on **AWS RDS** **(PostgreSQL)** and deploy a dashboard online using **Streamlit**.

The final product is a dashboard accesible by any browser containing valuable information about used car prices in Brazil. In a business perspective, it can be used as a benchmark for several companies that work into or depend on this market.


> [Final app: Open Dashboard for Used Cars Prices in Brazil](https://carscraping.streamlit.app/)

## Tech Stack

1) I use **venv** for dependencies management.


2) **Scrapy** is a framework for webscraping. This framework allows **multiple crawlers** configuration and different parsing schemes.


## Architecture

1) After retrieving and parsing the data from crawlers, it is stored on a json file.


2) This json file is transformed using pandas and the data is loaded into the data warehouse (AWS RDS) under a determined schema. 


3) Security rules were set to ensure that streamlit cloud could acces the dashboard.


4) I have built a dashboard app using Streamlit and deployed it to the Streamlit cloud. This step required the AWS RDS setup.


