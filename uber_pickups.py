#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np


# In[2]:


st.title('Uber pickups in NYC')


# In[3]:


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# In[4]:


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')


# In[6]:


@st.cache
def load_data(nrows):
    data_load_state.text("Done! (using st.cache)")


# In[7]:


st.subheader('Raw data')
st.write(data)


# In[8]:


st.subheader('Number of pickups by hour')


# In[9]:


hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]


# In[10]:


st.bar_chart(hist_values)


# In[11]:


st.subheader('Map of all pickups')


# In[12]:


st.map(data)


# In[13]:


st.subheader('Map of all pickups')
st.map(data)


# In[14]:


hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)


# In[15]:


hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h


# In[16]:


st.subheader('Raw data')
st.write(data)


# In[17]:


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


# In[ ]:




