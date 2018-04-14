
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


# In[2]:


# Series trong pandas giống array 1 chiều
s = pd.Series([1, 3, 5, np.nan, 6, 8])

# Create datatime in pandas 
dates = pd.date_range('20180308', periods=6)

# Create table with 
df = pd.DataFrame(np.random.rand(6,4), index=dates, columns = list('ABCD'))


# In[3]:


# View
n = 4
# View head <=> SELECT * TOP n
df.head(n)

# View index
df.index

# View Columns Name
df.columns

# Get length of columns name
len(df.columns)

# Get describe of columns
df.describe()

# Tranpose of matrix
df.T
    # or
df.transpose()

#Sort 
sort_colName = 'A'
df.sort_values(sort_colName)


# In[73]:


## SELECT


# In[74]:


# Select A
col_name = 'A'
df[col_name]

# Chú ý : Iloc khác loc chỗ loc chỉ cho phép Input là String
# Trong khi loc cho phép input là int
# Select with index, index of values is a date 

df['20180202' : '20180310']
row_from = '20180302'
row_to = '20180310'

col_from = 'A'
col_to = 'C'

df.loc[row_from : row_to, col_from : col_to]


# Select with iloc
row_from = 0
row_to = 3

col_from = 0
col_to = 3

df.iloc[row_from: row_to, col_from : col_to]


# In[153]:


# Filter Data

# One condition
df[df.A > 0.3]

df[df.iloc[:,0] > 0.3]

temp = df[ df > 0.3 ]

# Reindex
# Add Columns E into Table
df1 = df.reindex(index = dates[0:3], columns=list(df.columns) + ['E'])

# Fix Values for new columns
df1.loc[:, 'E'] = 1
df1

# Drop columns with 1 is axis (Columns mean)



# In[156]:


temp = np.cumsum
temp

