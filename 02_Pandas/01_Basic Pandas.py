
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


# Create Table

## From Array

s = pd.Series([1,2,3, np.nan, 8, 8])
dates = pd.date_range('20180228', periods = 6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

## From Lib Type
df2 = pd.DataFrame({
    'A' : 1.,
    'B' : pd.Timestamp('20180306'),
    'C' : np.array([3] *4, dtype='int32'),
    'E' : pd.Categorical(['test1', 'test2','test3','test4']),
    'F' : 'foo'
})

df2 = df.copy()


# In[4]:


# Basic GET 

## Get first 2 rows
df2.tail(2)

## Get index of Table
df.index

## Get columns Name
df.columns

## Get values of Table. Output is an array
df2.values

## Get information about data 
df2.describe()

## Get Data with in Array Type or Matrix type
df2.values


# In[5]:


# Condition : 
col_name = ['A','B']
from_row = 0
to_row = 3

index_from = '20180227'
index_to = '20180302'

# 1. Select 
## 1.1 Select columns 
df2.A
df2['A']

## 1.2 Select rows
df2[:][1:3]

## 1.3 Select Index
## .loc là loại filter theo index
df2.loc[index_from : index_to, col_name]
df2.loc[: , col_name]
df2.loc['20180228':'20180303',['A','D', 'B']]

## 1.4 Select rows and columns
df2[from_row : to_row][col_name]
df2[index_from : index_to][col_name]


# Select Data in rows 3
rows = 3
df.iloc[rows]

column = 'A'
df.iloc[rows][column]

df.iloc[from_row : to_row][col_name]

#Get 3 rows and 3 columns
df.iloc[[1,2,3], [1,2,3]]

# Get a values in the array
df2.iat[1,2]


# In[21]:


df2.iloc[:3]['A'] = df2.iloc[:3]['A'].apply(lambda x: min(x, 0))
df2


# In[16]:


df2


# In[15]:


# Get table with condition
df[df>0]


# In[8]:


df2 = df.copy()


# In[9]:


df2


# In[10]:


# Insert, Delete, Update

# 1. Column
## 1.1 Insert
data = ['A','A','B','B','B','C']
df2['new_col1'] = data

df2['new_col2'] = data

## 1.2 Delete
col_delete = 'new_col1'
df2 = df2.drop(col_delete, 1)

df2


# In[11]:


# UPDATE DATA

## Update data at column A, with index = '20180304'
in_index = '20180304'
in_colName = 'A'

df2.at[in_index, in_colName] = 'A'
df2


# In[13]:


# Search
search_colName = 'new_col2'
search_values = ['A','C']

filter_rows = df2[search_colName].isin(search_values)

df2[filter_rows]


# In[ ]:


# SORT

# Sort with index
df2.sort_index(axis=0, ascending=False)

# Sort with column "new_colName"
df2.sort_values(by='new_colName', ascending=True)


# In[16]:


df2.iloc[:,0:3]


# In[32]:


df2.A*100

