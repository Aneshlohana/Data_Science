# import libaries
from turtle import width
import streamlit as st
import plotly as px
import pandas as pd 

# import dataset 
st.header('Steamlist and plotly ko mila ka app SAdddiiiii')
df = px.data.gapminder()
st.write(df)
st.write(df.columns)

# summary stat
st.write(df.describe())

# data management
year_values = df['year'].unique().tolist()
year = st.selectbox("Which year should we plot?",year_values,0)
df = df[df['year']== year]

# ploting
fig = px.scatter(df, x= 'gdpPercap', y = 'lifeExp' , size='pop',color='country',hover_data='country',log_x= True , size_max=55,range_x=[100,100000],range_y=[20,90])
fig.update_layout(width=800)
st.write(fig)
