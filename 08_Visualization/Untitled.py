
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


from mpl_toolkits.mplot3d import Axes3D
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm


# In[3]:


plt.rcParams['font.family'] = 'Sans-serif' #全体のフォントを設定
plt.rcParams["figure.figsize"] = [20, 12]
plt.rcParams['font.size'] = 12 #フォントサイズを設定 default : 12
plt.rcParams['xtick.labelsize'] = 15 # 横軸のフォントサイズ
plt.rcParams['ytick.labelsize'] = 15


# In[4]:


x = np.linspace(-5, 5, 21)
X, Y = np.meshgrid(x, x)
Z = -5 + 3*X - 0.5 * Y + 8 * np.random.normal(size = X.shape)

#Plot 
fig = plt.figure()
ax = fig.gca(projection = '3d')
surf = ax.plot_surface(X,Y,Z, cmap=plt.cm.coolwarm, rstride = 1, cstride=1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


# ## 1. Vẽ chart 3D, Z = 1. X, Y cho trước

# In[5]:


X = [0, 10, 20]
Y = [100, 200, 300]

XX, YY = np.meshgrid(X, Y)

ZZ = np.reshape([1]* XX.shape[0] * XX.shape[1], XX.shape)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(XX, YY, ZZ, cmap=plt.cm.coolwarm, rstride=1, cstride=1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


# In[6]:


XX


# In[7]:


YY


# In[8]:


plt.plot(XX, YY, 'bo')


# meshgrid.
# 
# Từ mảng 
# X = [0, 10, 20]
# Y = [100, 200, 300]
# 
# Tạo ra mảng có dạng :
# 
# XX =
# [[0, 10, 20],
# [0, 10, 20]
# [0, 10, 20]]
# 
# YY =
# [[100, 100, 100],
# [200, 200, 200],
# [300, 300, 300]].
# 
# Khi biểu diễn XX, YY lên mặt phẳng 2 chiều, ta có như hình trên

# ## 2. Vẽ đồ thị hình Sin của Y = SIN(X) trên 3D

# In[9]:


X = np.linspace(0, 30, 100)
plt.rcParams["figure.figsize"] = [20, 3]
plt.plot(X, np.sin(X))


# In[10]:


# Tạo X có 200 giá trị
X = np.linspace(0, 30, 100)

XX1, XX2 = np.meshgrid(X, X)
plt.rcParams["figure.figsize"] = [20, 8]

YY = np.sin(XX1)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(XX1, XX2, YY, cmap=plt.cm.coolwarm, rstride=1, cstride=1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


# ## 3. Normal Distribution trên 3D

# In[34]:


a = np.sort(np.random.normal(loc=0, scale=20, size=1000).round())


# ### Trên 1 mặt phẳng

# In[35]:


aa1, aa2 = np.meshgrid(a, a)
pa = np.reshape(aa1.shape[0] * aa1.shape[1] * [1], aa1.shape)

plt.rcParams["figure.figsize"] = [20, 12]
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(aa1, aa2, pa, cmap=plt.cm.coolwarm, rstride=1, cstride=1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


# ## X và Z

# In[36]:


temp = pd.DataFrame(a, columns = ['value'])
temp['temp'] = [1] * len(temp)
ZX_temp = temp.groupby('value').count().values
ZX1, ZX2 = np.meshgrid(ZX_temp, ZX_temp)


# In[31]:


pa = np.sin(aa1)


# In[33]:


plt.rcParams["figure.figsize"] = [20, 12]
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(aa1, aa2, pa, cmap=plt.cm.Blues, rstride=1, cstride=1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

