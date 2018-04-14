
# coding: utf-8

# In[9]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[10]:


# Create test data
# Create const variance
a, b, c, d = [4, 2, 5, 7]
num_arr = 100

# Create random values X1,X2,X3 and Y with Y = aX1 + bX2 + cX3 + dX4 with X4 of values is 1
X1, X2, X3, X4 = [np.random.rand(100), np.random.rand(100), np.random.rand(100), np.ones(100)]
Y = a* X1 + b*X2 + c*X3 + np.random.rand(100)* X4

# Import data into dataframe and transposing data
dataFrame = pd.DataFrame({
    'X1' : X1,
    'X2' : X2,
    'X3' : X3,
    'X4' : X4,
    'Y' : Y
})

dataFrame


# In[11]:


# Cai thien ham Training, su dung cong thuc nhan 2 matrix
# Rows number in Training Data
m = dataFrame.X1.count()
# Columns number in Training Data
n = len(dataFrame.columns) -1
# Learning_rate
learning_rate = 0.02
# Set random for theta
theta = np.random.rand(n)
# To save values of cost function each loop
cost_arr = []

def predict(datafrm, theta):
    col_start = 0
    col_end = 4
    # Get first 4 columns of table and transpose dimension
    get_trainData = datafrm.iloc[ : , col_start : col_end]
    return np.dot(theta, get_trainData.T)

def cost_update(datafrm, theta):
    yhat = predict(datafrm, theta)
    y = datafrm.Y
    return np.sum((yhat-y)**2)/(2*m)

y = dataFrame.Y

for i in range(6000):
    yhat_train = predict(dataFrame, theta)
    for x in range(n):
        theta[x] = theta[x] - learning_rate*np.sum((yhat_train-y)*dataFrame.iloc[ : , x])/m
    cost_arr.append(cost_update(dataFrame, theta))
    
cost_arr
plt.plot(cost_arr)


# In[12]:


theta

