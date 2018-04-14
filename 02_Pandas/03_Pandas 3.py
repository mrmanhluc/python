
# coding: utf-8

# In[143]:


import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt


# In[144]:


train_data = pd.read_csv(r'D:\temp\00_data\train.csv')
test_data = pd.read_csv(r'D:\temp\00_data\test.csv')

full_data = [train_data, test_data]

# Check null for all indexs
temp = np.count_nonzero(train_data[train_data.Cabin.isna() == np.True_]['Cabin'])
temp


# In[145]:


train_data.Cabin.isnull().sum()


# In[189]:


# Tính tổng Null
col_name = list(train_data.columns)
value_name = []

for x in list(train_data.columns):
    value_name.append(train_data[x].isnull().sum())
    
null_status = pd.DataFrame(np.array(count_null)).transpose()
null_status.columns = columns1

# plt.bar(columns1 ,count_null,width = 0.3, alpha=0.5)
null_status

# XỬ lý null cho cabin


# In[104]:


np.arraytrain_data.columns

