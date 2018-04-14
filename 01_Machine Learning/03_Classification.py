
# coding: utf-8

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt
import math


# In[5]:


a = np.arange(0., 1., 0.01)
b = (np.random.rand(100) - .5) / 100
a += b
c = a > .5
d = np.random.rand(100) > .1
e = [c[i] if d[i] else not c[i] for i in range(100)]
plt.plot(e, 'ro')

# Phuong trinh ham predict, hình dáng đồ thị có hình như sau

X = a
Y = np.array(e)

plt.plot(X, Y, 'ro')


# In[6]:


def f_yhat(x, theta):
    z = np.dot(theta.T, x) 
    return 1/(1 + np.exp(-z))

def f_cost(x, y, theta):
    m = len(x)
    yhat = f_yhat(x, theta)
    
    return (-1/m) * np.sum(y * np.log(yhat) + (1 - y) * np.log(1 - yhat))

def f_training(x, y, theta, learning_rate, train_loop):
    m = len(x)
    cost_arr = []
    
    for i in range(train_loop):
        yhat = f_yhat(x, theta)
        t0 = theta[0] - learning_rate * np.sum((yhat - y) * x[0])/m
        t1 = theta[1] - learning_rate * np.sum((yhat - y))/m
        theta = np.array([t0, t1])
        cost_arr.append(f_cost(x, y, theta))
        
    return theta, cost_arr


# In[7]:


X = np.concatenate((X, np.ones(len(X))), axis = 0).reshape(2, len(X))

Theta = np.random.rand(2)

train_theta, cost = f_training(X, Y, Theta, 0.001, 10000)

train_theta


# In[8]:


# Cost function graph
plt.plot(cost)


# In[11]:


# Phương trình dự đoán

Y_h = f_yhat(X, train_theta)

plt.plot(X[0], Y_h)
plt.plot(X[0], Y, 'ro')


# In[7]:


from sklearn import datasets, linear_model

regr = linear_model.LogisticRegression(fit_intercept=False)
t = np.reshape(a, (-1, 1))
regr.fit(t, Y)

#print(regr.coef_)
print(regr.coef_)

Theta = np.array([1.06474347, 0])
Yhat1 = f_yhat(np.array(X), Theta)

plt.plot(Yhat1, X[0])
plt.plot(X[0], Y, 'ro')

