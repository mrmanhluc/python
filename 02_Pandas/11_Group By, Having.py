
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


d = {
    'one': [1, 1, 1, 1, 1],
    'two': [2, 2, 2, 2, 2],
    'letter': ['a', 'a', 'b', 'b', 'c']
}
df = pd.DataFrame(d)
df


# In[5]:


# Group by with letter and sum
df.groupby('letter').sum()


# In[8]:


# Group by with mutil column
letter_one = df.groupby(['letter', 'one']).sum()


# In[14]:


# Data type cua group by la MultiIndex
letter_one


# In[13]:





# In[17]:


a = {
    1: 'a value',
    'key': 31.12,
    (1, 'immutable'): range(20)
}
str 

