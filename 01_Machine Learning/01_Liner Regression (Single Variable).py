
# coding: utf-8

# In[ ]:


# Phương trình hàm bậc 1 y = ax + b


# In[2]:


import numpy as np
import matplotlib.pyplot as plt

#Create sample data
X = np.random.randn(100)
Y = X*5 + np.random.randn(100)


# In[3]:


plt.plot(X, Y, 'bo')


# In[4]:


#Step 1 : select random a and b

def yhat(a, b):
    return a*X + b

def cost(yhat):
    return (np.sum((yhat-Y)**2))/((2*m))

m = 100
learning_rate = 0.1
a=4
b=5

cost_arr = []

for x in np.arange(100):
    temp = yhat(a,b)
    a = a - learning_rate * np.sum((temp - Y)*X)/m
    b = b - learning_rate * np.sum((temp - Y))/m
    cost_arr.append(cost(yhat(a,b)))
    
cost_arr

plt.plot(cost_arr)


# In[5]:


plt.plot(X,Y, 'ro')
x0 = np.linspace(-3,3, 100)
y0 = a*x0 + b

plt.plot(x0, y0)

