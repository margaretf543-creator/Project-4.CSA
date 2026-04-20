import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Car Sales Advertisements Dashboard')
st.write('Exploring car sales advertisement data in the US.')

show_affordable = st.checkbox('Show only cars under $50,000')

if show_affordable: 
    df_filtered = df[df['price'] < 50000]
else:
    df_filtered = df 

# histogram of prices
st.subheader('Distribution of Car Prices')
st.write('This histogram shows how car prices are distributed across all listings.')
fig = px.histogram(df_filtered, x='price', title='Distribution of Car Prices')
st.plotly_chart(fig, key='price_hist')

# histogram by condition
st.subheader('Number of Cars by Condition')
st.write('This chart shows how many cars are listed in each condition category.')
fig = px.histogram(df_filtered, x='condition', title='Number of Cars by Condition')
st.plotly_chart(fig, key='condition_hist')

# scatter plot price vs model year
st.subheader('Price vs Model Year')
st.write('This scatter plot shows the relationship between car price and model year, colored by condition.')
fig = px.scatter(df_filtered, x='model_year', y='price',
                title='Price vs Model Year',
                color='condition')
st.plotly_chart(fig, key='model_year_scatter')