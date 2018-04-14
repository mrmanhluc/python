
# coding: utf-8

# In[96]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[285]:


s = pd.Series([1,3,5,6,np.nan, 6,7])
s = [1,3,5,6,np.nan,7,7]

date = pd.date_range('20180302', periods=6)
date

df2 = pd.DataFrame({
            'A' : 2,
            'B' : pd.Timestamp('20180302'),
            'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
            'D' : np.array([3] * 4, dtype='int32'),
            'E' : pd.Categorical(["Test", "Train", "test", "train"]),
            'F' : 'foo'
})


# In[286]:


df2[:]['E'] = df2[df2.E == "Test"]['E'] = 0


# In[287]:


df2[df2.E == "Test"]['E']


# In[288]:


df2

