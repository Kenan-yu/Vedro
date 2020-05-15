#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import matplotlib.pyplot as plt


# In[11]:


data_url = "https://raw.githubusercontent.com/FundamentalsPythonYello/data-analysis-0/master/Sales_Data/Sales_April_2019.csv"
df = pd.read_csv(data_url, index_col = 0)
df[:5]


# In[12]:


df['Month'] = 'column'
df.head()


# In[13]:


df['Month'] = df['Order Date'].str[0:2]
df.head()


# In[25]:


df_nan = df[df.isna().any(axis=1)]
df = df.dropna(how = 'all')
df = df[df['Order Date'].str[0:2] != 'Or']


# In[32]:


df['Month'] = df['Month'].astype('int32')
df.head()


# # Convert to right type

# In[33]:


df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'])
df['Price Each'] = pd.to_numeric(df['Price Each'])


# In[34]:


df['Sales'] = df['Quantity Ordered'] * df['Price Each']
df.head()


# # Data Exploration!

# In[60]:


df.groupby('Month').sum()['Sales']


# In[62]:


container = df.groupby('Month').sum()
x = range(1, 3)
y = container['Sales']
plt.bar(x, y, color = 'green')


# In[ ]:




