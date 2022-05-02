#!/usr/bin/env python
# coding: utf-8

# In[10]:


import streamlit as st

import sys


# In[12]:


header = st.container()

dataset = st.container()

features =st.container()

modeltraining = st.container()


# In[1]:


import pandas as pd 
import altair as alt


# In[2]:


url = "https://gist.githubusercontent.com/Tulluripallavi/983092b3b60760198dc778117141ac55/raw/bbba5e8e8f1c94e297c492cd33975aa97da1f056/salesdisaster.csv"
mpg = pd.read_csv(url)


# In[ ]:


with header:
    st.title("Data visulization Project")


# In[14]:


'''with dataset:
    st.title("Data visulization Project 1")
    # Encoding Data using Color and Size
    chart = (alt.Chart(mpg)# including the csv file
    .encode(
    x='Sales Agent ID', # adding the X value
    y='Sales',# adding the Y value
    color = "State",# adding the color value
    tooltip=['Sales Agent ID', 'Sales', 'State']
    )
    .mark_circle()# Making it as circular representation
    )
    chart.encode()# displaying the data'''
selection= alt.selection_multi(fields=["Sales Agent ID", "Sales"],bind='legend')
chart3 = (alt.Chart(mpg)
    .encode( 
    y='Sales',
    color = "State",
    #opacity=alt.condition(selection, alt.value(1),alt.value(0)),
    ).add_selection(selection)
  .mark_circle()
)
chart3.encode(x='Sales Agent ID')|chart3.encode(x='Zip Code')


# In[5]:




chart6 = (alt.Chart(mpg)# including the csv file
    .encode(
    x='Sales Agent ID', # adding the X value
    y='Sales',# adding the Y value
    color = "State",# adding the color value
    tooltip=['Sales Agent ID', 'Sales', 'State']
    )
  .mark_bar()# Making it as circular representation
  .properties(width = 500)
)
chart6.encode(x='Sales Agent ID')|chart6.encode(x='Zip Code')


# In[6]:


chart5= (alt.Chart(mpg)# including the csv file
    .encode(
    y='Sales',# adding the Y value
    color = alt.Color("location", legend=None),# adding the color value
    tooltip=['Sales Agent ID', 'Sales', 'State']
    )
  .transform_loess("Sales Agent ID", "Sales", groupby = ["State"] )
  .mark_line()# Making it as circular representation
  
)
chart5.encode(x='Sales Agent ID')|chart5.encode(x='Sales Agent ID')


# In[7]:


chart7 = (alt.Chart(mpg)# including the csv file
    .encode(
    x='Sales Agent ID', # adding the X value
    y='Sales',# adding the Y value
    color = "State",# adding the color value
    tooltip=['Sales Agent ID', 'Sales', 'State']
    )
  .mark_rect()# Making  representation
)
chart7.encode(x='Sales Agent ID')|chart7.encode(x='Zip Code')


# In[8]:


chart8 = (alt.Chart(mpg)# including the csv file
    .encode(
    x='Sales Agent ID', # adding the X value
    y='Quantity',# adding the Y value
    color = "State",# adding the color value
    tooltip=['Sales Agent ID', 'Quantity', 'State']
    )
  .mark_boxplot()# Making it as boxplot representation
)
chart8.encode(x='Sales Agent ID')|chart8.encode(x='Zip Code')


# In[9]:


selection= alt.selection_multi(fields=['State'],bind='legend')
chart = (alt.Chart(mpg)
    .encode( 
    y='Sales',
    color = "State",
    opacity=alt.condition(selection, alt.value(1),alt.value(0)),
    ).add_selection(selection)
  .mark_point()
)
chart.encode(x='Sales Agent ID')|chart.encode(x='Zip Code')


# In[ ]:


