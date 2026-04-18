import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Car Sales Advertisements Dashboard')
st.write('Exploring car sales advertisement data in the US.')

show_affordable = st.checkbox('Show only cars under 50k')

if show_affordable: 
    df_filtered = df[df['price'] < 50000]
else:
    df_filtered = df 

# histogram of prices
st.subheader('Distribution of Car Prices')
fig = px.histogram(df, x='price', title='Distribution of Car Prices')
st.plotly_chart(fig, key='price_hist')

# histogram by condition
st.subheader('Number of Cars by Condition')
fig = px.histogram(df, x='condition', title='Number of Cars by Condition')
st.plotly_chart(fig, key='condition_hist')

# scatter plot price vs model year
st.subheader('Price vs Model Year')
fig = px.scatter(df, x='model_year', y='price',
                title='Price vs Model Year',
                color='condition')
st.plotly_chart(fig, key='model_year_scatter')