
# coding: utf-8

# In[110]:


import numpy as np
import pandas as pd
import scipy.stats as st


# In[85]:


data = pd.DataFrame(np.random.normal(loc = 80, scale=30, size= 1000).round(), columns=['val'])
data['count'] = 1 * len(data)


# In[86]:


data['val'].plot.hist()


# In[87]:


data.groupby(['val']).count().plot()


# In[88]:


mean = data.values.mean()
std = data.values.std()


# In[107]:


data['convert'] = [((x-mean)/(std)) for x in data.val]


# In[109]:


data.groupby('convert').count().val.plot()
plt.plot(mean, 'r--')


# In[94]:


data

