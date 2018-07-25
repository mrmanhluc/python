
# coding: utf-8

# # Gradient of  Sigmoid Function

# ## 1. Sigmoid Function and Gradient of Sigmoid 
# 
# $$
# σ(z) = \frac{1}{1+\exp{-Z}}
# $$
# 
# #### Gradient of Sigmoid
# $$
# \frac{dσ(x)}{d(x)} =σ(x)⋅(1−σ(x))
# $$

# In[4]:


import numpy as np
import matplotlib.pyplot as plt


# In[10]:


def sigmoid(z):
    return 1/(1 + np.exp(-z))

def gradient_sigmoid(z):
    return sigmoid(z) * (1 - sigmoid(z))


# In[11]:


x = range(-20, 20)

y = [gradient_sigmoid(i) for i in x]

plt.plot(x,y)

print(y[10])


# ### Kết luận : 

# Giá trị đạo hàm của Sigmoid Function luôn có giá trị <0.25 trong khoảng từ -5;5.
# 
# Ngoài khoảng này, giá trị Sigmoid Function ~ 0. Vì vậy Learning gần như không thay đổi.
# 
# Vì vậy, cần chuẩn hóa miền giá trị về 0 trước khi thực hiện training.
