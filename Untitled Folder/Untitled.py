
# coding: utf-8

# In[2]:


from tableausdk import *
from tableausdk.Server import * 
from tableausdk.Extract import *


# In[4]:


tde_file = Extract('ExtractFile.tde')


# In[13]:


table_def = TableDefinition()
table_def.addColumn('Column1', Type.CHAR_STRING)


# In[14]:


tde_file.close()


# In[3]:


x = 'abc'
x[-1]


# In[4]:


x = [int(x) for x in str(input()).split(" ")]


# In[16]:


x = [2, 2, 3, 5, 2]


# In[17]:


count_left, count_right = 0, 0

for i in range(len(x)):
    count_right += x[i]

for i in range(len(x)):
    if(count_left == count_right):
        print(i)
        break
    if count_left > count_right:
        print('False')
        break
    count_left += x[i]
    count_right -= x[i]

