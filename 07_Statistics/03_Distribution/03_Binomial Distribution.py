
# coding: utf-8

# # Binomial Distribution
# 
# ----
# 
# ## 1. Tổng quan : 
# Nếu các biến X tuân theo luật phân phối nhị thức với parameter :
# - n ∈ ℕ (n là số lượng phép thử, ℕ số lần lặp lại phép thử)
# - p ∈ [0,1] : p xác xuất True or False 
# - k : Số lần thành công trong n phép thử đó.
# 
# #### Kí hiệu : X ~ B(n, p). B viết tắt Binomial
# 
# Ví dụ : Tung 5 đồng xu (n = 5), xác xuất xuất hiện mặt trước và sau là như nhau (p = 0.5), ta thu được 2 đồng sấp, 3 đồng ngữa.
# Gọi k là số mặt ngữa, ta có k = 2.
# 
# Thực hiện việc tung 5 đồng xu trên 100 lần (N = 100), ta thu được tập k chứa các phần tử có giá trị  p ∈ [0,5].
# 
# ## 2. Probability
# 
# Xác xuất để có k lần thành công : 
# \begin{equation*}
# Pr(X=k)   = C{n \choose k} p^k (1-p)^{ n-k}
# \end{equation*}
# 
# Với k = 0,1,2,...,n thì : (combinaisons - Tổ hợp)
# \begin{equation*}
# C{n \choose k} = \frac{n!}{k!(n-k)!}
# \end{equation*}

# In[1]:


import numpy as np
import pandas as pd
from scipy.stats import binom
import matplotlib.pyplot as plt


# ## 3. Công thức
# 
# Trong đó : 
# - Factoria : Function giai thừa
# - Combinasisons : Function tính tổ hợp 
# - Pr_Binomail : Function tính xác suất thành công với (n : số phép thử mỗi lần, p : Xác xuất thành công, k : số thành công)

# In[61]:


# factorial - Giai thừa
def factoria(n):
    x = 1
    if n==0:
        return 1
    for i in range(n):
        x = x * (i+1)
    return x

# Combinaisons - Tổ hợp
# Từ 1 hộp 4 viên xanh đỏ tím vàng, có bao nhiêu cách lấy ra 2 viên, biết (xanh đỏ) (đỏ xanh) là một
def combinaisons(n, k): 
    return (factoria(n) / ((factoria(k) * (factoria(n-k)))))

# Probability 
def pr_binomial(n, p, k):
    '''
        n : Số phép thử trong 1 lần
        p : Xác xuất thành công mỗi phép thử
        k : Số lần thanahf công trong mỗi phép thử
    '''
    return combinaisons(n, k) * np.power(p,k) * np.power(1-p, n-k)


# ## 4. Example
# 
# ### 4.1 Example 1 : Tung 1 đồng xu với xác xuất 0.5
# Tạo Sample Data đếm số mặt sấp và ngữa khi tung 1 đồng xu.
# 
# Trong đó : 
# - n = 1. (Tung1 đồng xu)
# - p = 0,5 Xác xuất xuất hiện 2 mặt là như nhau
# - N = 1000. Thực hiện 1000 phép thử
# 
# K có 2 giá trị :
# - 0 : không có mặt ngữa nào xuất hiện
# - 1 : Có 1 mặt ngữa xuất hiện
# 
# 【ASK】Tính xác xuất : 
# - Pr(0)
# - Pr(1)

# In[22]:


N = 1000
sample = pd.DataFrame(np.random.binomial(n = 1, p = 0.5, size = N), columns=['count'])
sample['temp'] = [1] * len(sample)


# #### 4.1.1 Tập data ghi lại kết quả sau mỗi lần tung đồng xu

# In[58]:


pd.DataFrame(sample['count'].head())


# #### 4.1.2 Xác xuất được tính theo data

# In[59]:


sample.groupby('count').count()/N


# In[30]:


print('Xác xuất xuất hiện K = 0 và K = 1 là như nhau = 0.5')
plt.hist(sample['count'])


# #### 4.1.3 Xác xuất tính theo công thức

# In[64]:


# n = 1 , p = 0.5, k = 1)

print('Xác xuất suất hiện mặt ngữa là : '+str(pr_binomial(1, 0.5, 1)))


# ### 4.2 Example 2 : Tung 5 đồng xu với xác xuất 0.5
# 
# Tạo Sample Data đếm số mặt sấp và ngữa khi tung 1 đồng xu.
# 
# Trong đó : 
# - n = 5. (Tung 5 đồng xu)
# - p = 0,5 Xác xuất xuất hiện 2 mặt là như nhau
# - N = 1000. Thực hiện 1000 phép thử
# 
# K có 5 giá trị :
# - 0 : không có mặt ngữa nào xuất hiện
# - 1 : Có 1 mặt ngữa xuất hiện
# - 2 : Có 2 mặt ngữa xuất hiện
# - 3 : Có 3 mặt ngữa xuất hiện
# - 4 : Có 4 mặt ngữa xuất hiện
# - 5 : Có 5 mặt ngữa xuất hiện
# 
# 【ASK】Tính xác xuất : 
# - Pr(k = 0)
# - Pr(k = 1)
# - Pr(k = 2)
# - Pr(k = 3)
# - Pr(k = 4)
# - Pr(k = 5)

# In[81]:


N = 1000
sample1 = pd.DataFrame(np.random.binomial(n = 5, p = 0.5, size = N), columns = ['count'])
sample1['temp'] = [1] * len(sample1)


# #### 4.2.1 Tập data ghi lại kết quả sau mỗi lần tung đồng xu

# In[86]:


pd.DataFrame(sample1['count'][0:10])


# #### 4.1.2 Xác xuất được tính theo data

# In[91]:


sample1.groupby('count').count()/N


# In[93]:


(sample1.groupby('count').count()/N).plot()


# #### 4.1.3 Xác xuất tính theo công thức

# In[117]:


pr = []
for i in range(6):
    pr.append(pr_binomial(5, 0.5, i))

pd.DataFrame(pr).plot()


# #### So sánh xác xuất được tính dựa vào data thực tế và xác xuất dựa vào công thức, ta thấy kết quả xấp xỉ nhau

# In[120]:


print('Kết quả được tính dựa theo công thức : ')
pd.DataFrame(pr)


# In[122]:


print('Kết quả được tính dựa vào data : ')
sample1.groupby('count').count()/N


# ### 4.3 Example 3 : Tung 5 đồng xu với xác xuất 0.3
# 
# #### Assumptions : Đồng xu không đều, mặt sấp xuất hiện ít hơn mặt ngữa. Xác xuất xuất hiện mặt sấp là 0.3
# 
# Tạo Sample Data đếm số mặt sấp và ngữa khi tung 1 đồng xu.
# 
# Trong đó : 
# - n = 5. (Tung 5 đồng xu)
# - p = 0,3 Xác xuất xuất hiện 2 mặt là như nhau
# - N = 1000. Thực hiện 1000 phép thử
# 
# K có 5 giá trị :
# - 0 : không có mặt ngữa nào xuất hiện
# - 1 : Có 1 mặt ngữa xuất hiện
# - 2 : Có 2 mặt ngữa xuất hiện
# - 3 : Có 3 mặt ngữa xuất hiện
# - 4 : Có 4 mặt ngữa xuất hiện
# - 5 : Có 5 mặt ngữa xuất hiện
# 
# 【ASK】Tính xác xuất : 
# - Pr(k = 0)
# - Pr(k = 1)
# - Pr(k = 2)
# - Pr(k = 3)
# - Pr(k = 4)
# - Pr(k = 5)

# In[130]:


sample4 = pd.DataFrame(np.random.binomial(n = 5, p = 0.3, size = N), columns = ['count'])
sample4['temp'] = [1] * len(sample4)


# ## Analytics : 
# 
# Từ đồ thị, thấy rằng xác xuất xuất hiện mặt sấp = 1 trong 5 lần tung là cao nhất.

# In[134]:


sample4.groupby('count').count().plot()


# In[136]:


print('Xác xuất tính theo data : ')
sample4.groupby('count').count()/N


# In[138]:


print('Xác xuất tính theo công thức : ')
pr = []
for i in range(6):
    pr.append(pr_binomial(5, 0.3, i))

pd.DataFrame(pr)


# ## 5. Example from Real world
# 
# Bài toán thực tế : 
# 
# Dây chuyển sản xuất Iphone gồm 10 Robot, cứ mỗi giờ tình trạng của Robot được update với Status [Hỏng, Chạy tốt]
# * Xác xuất một máy có khả năng hỏng mỗi giờ 10%.
# 
# Tìm xác xuất các trường hợp sau : 
# * TH1. Một máy hỏng 
# * TH2. 2 máy hỏng cùng lúc
# * TH3. 3 máy hỏng cùng lúc
# * TH4. 4 máy hỏng cùng lúc
# ....
# * TH10. 10 máy hỏng cùng lúc
