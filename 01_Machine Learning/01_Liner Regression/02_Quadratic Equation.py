
# coding: utf-8

# In[117]:


#Phương trình hàm bậc 2. y = ax^2 + bx + c
import numpy as np
import matplotlib.pyplot as plt


# In[118]:


a = 2
b = -2
m = 100

X = np.random.randn(m) * 10
Y = a*X**2 + b*X + np.random.randn(m) * 100

#Y = Y / np.max(Y)

plt.plot(X,Y,'ro')


# In[119]:


def Y_Hat(a,b,c,x):
    return a*x**2 + b*x + c

def cost(x,y,a,b,c):
    y_hat = Y_Hat(a, b, c, x)
    return np.sum((y_hat - y)**2)/(2*m)

a = 3
b = 4
c = 5
learning_rate = 0.00002

cost_arr = []

for i in np.arange(2000000):
    y_hat = Y_Hat(a, b, c, X)
    a = a - learning_rate*(np.sum((y_hat - Y)*X**2))/m                     
    b = b - learning_rate*(np.sum((y_hat - Y)*X))/m
    c = c - learning_rate*(np.sum((y_hat - Y)))/m
    cost_arr.append(cost(X,Y,a,b,c))


# In[120]:


plt.plot(cost_arr)


# In[121]:


print (a,b,c)


# In[122]:


x0 = np.linspace(-30,30,20)
y0 = Y_Hat(a,b,c, x0)
plt.plot(x0,y0)

plt.plot(X, Y, 'ro')


# In[123]:


from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


# In[124]:


XX = X.reshape(m, 1)
poly = PolynomialFeatures(degree=2)
XX = poly.fit_transform(XX)
model = LinearRegression()
model.fit(XX, Y)


# In[125]:


temp = model.predict(XX)


# In[126]:


c, b, a = model.coef_


# In[127]:


x0 = np.linspace(-30, 30, 20)
y0 = Y_Hat(a,b,c, x0)

plt.plot(x0,y0)
plt.plot(X,Y, 'ro')


# In[129]:


print(a, b, c)

