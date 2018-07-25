
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


r1 = [7, 2, 3, 6, 8]
r2 = [5, 1, 2, 3, 4]

y = [10, 2, 3, 7, 8]


# In[30]:


count = 0

for i in range(1, len(r1)):
    count = count + r1[i]/np.log(i+1)


# In[33]:


count + r1[0]


# In[34]:


count = 0

for i in range(1, len(r2)):
    count = count + r2[i]/np.log(i+1)


# In[36]:


count + r2[0]

