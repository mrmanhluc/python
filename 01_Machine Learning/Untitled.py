
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def sigmoid(z):
    return 1/(1 + np.exp(-z))


# In[4]:


sigmoid(10)

