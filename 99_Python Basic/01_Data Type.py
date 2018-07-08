
# coding: utf-8

# # I. Basic Data Type
# 
# Sử dụng khi cần pair 2 columns với nhau.
# Name : ('Lực', 'Thư')
# Mark : (8, 9)

# In[51]:


import numpy as np
import pandas as pd


# # 1. List

# In[52]:


name = []
name.extend(['Name A', 'Name B', 'Name C'])

# Get data with index
name.index('Name A')

# Get last items - Stack (First in last out FILO) - FIFO - Queue
name.pop()


# In[53]:


x1 = [1,'b']
x2 = [2, 'a']

x = []
x.append(x2)
x.append(x1)

# Cũng có thể sử dụng sorted(x)
x.sort()


# ## 2. Tuple

# In[1]:


# Cách sử dụng Tubple  : Tuple data
x1 = ('luc', 'thu')
x2 = (8, 9)

# Ghép đôi 2 column với nhau (Pair)
z = zip(x1,x2)

# Select theo columns
for name, mark in z:
    print(name, mark)
    
z = zip(x1, x2)
# Select su dung enumerate
for name, mark in enumerate(z):
    print(name, mark)


# In[ ]:


x1.


# In[55]:


z = zip(x1, x2)
#Su dung enumerate với chỉ số i
for i, (name, mark) in enumerate(z):
    print(i, name, mark)
    
z = zip(x1, x2)
#Su dung enumerate
for i, pair in enumerate(z):
    print(i, pair)


# ### Chú ý khi sử dụng Tuple
# 
# str = 'abc' sẽ được coi là string str = 'abc', sẽ được coi là tuple

# In[149]:


nomal = 'simple'
error = 'training coma',

print(type(nomal))
print(type(error))


# # 3. Set

# In[56]:


setA = set(['A', 'B', 'C', 'D'])
setB = set(['A', 'B', 'E', 'F'])
setC = set(['A', 'B'])
# A Not in B
print(setC)

# Union set A va set B
setD = setA|setB
print(setD)

# Merger setA va setB
setE = setA & setB
print(setE)

# Test is subset
setC.issubset(setA)

# Update Set
#setC.update(['G'])
setC

# Discard 1 phan tu
setA.discard('A')
setA


# # Tổng hợp các type

# ### Kiểu Tuple
# x1 = ('student a', 'student b', 'student a')
# 
# ### Kiểu List
# x2 = ['student a', 'student b', 'student c']
# 
# ### Kiểu List, trong list chứa Tuple
# x3 = [('student a', 'student b', 'student c')]
# 
# ### Kiểu Sets 
# x4 = {'Student a', 'Student b', 'Student a', 'Student b'}
# 
# ### Kiểu Dict
# x5 = {
#          'col1': [1, 2, 3],
#          'col2': [3, 4, 5],
#      } 

# # 2. Pandas

# In[2]:


setA = set(['A', 'B', 'C', 'D'])
setB = set(['A', 'B', 'E', 'F'])
setC = set(['A'])

setC.issubset(setA)

