
# coding: utf-8

# # 1. Estimation type
# * Point estimation   - Ước lượng điểm của một tham số tổng thể là cách thức tính toán một giá trị đơn lẽ của tham số tổng thể dựa trên dữ liệu mẫu
# * Interval estimatin - Ước lượng khoảng
# 
# 
# ## Định lý nền tảng cho ước lượng
# * Cental limit theorem - Định lý giới hạn trung tâm
# 
# ```
# Một mẫu ngẫu nhiên gồm n quan sát được chọn từ một tổng thể không chuẩn tắc có trung bình là µ và độ lệch chuẩn là σ, nếu n lớn, thì phân phối mẫu của trung bình mẫu sẽ có phân phối xấp xỉ chuẩn tắc với trung bình là µ và độ lệch chuẩn .
# 
# ```
# 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# #### Chứng minh định lý Cental Limit theorem đối với Distribution bất kì
# 
# ### STEP 1 : Create random polpulation
# 
# * Tạo mẫu gồm N phần tử lưu cân nặng của dân số vùng A

# In[4]:


# Step 1. Tạo ra random quần thể N phần tử

N = 10000
polpulation = pd.DataFrame(np.random.randint(30, 100, size = N), columns=['Weight'])
polpulation['temp'] = [1] * N

# Mean of polpulation
X = polpulation.Weight.mean()
STD = polpulation.Weight.std()
VAR = polpulation.Weight.var()


# In[5]:


plt.plot(polpulation.groupby('Weight').count())
plt.axvline(x = X, linestyle = 'dashed', color = 'r')
plt.axvline(x = STD, linestyle = 'dashed', color = 'g')
plt.xlabel('Mean of polpulation is : ' + str(np.round(X,2)) + ' STD : '+str(np.round(STD,2)))
#plt.axvline(x = float(Mean_Male), linestyle = 'dashed',  linewidth=2, color = 'r')


# ### STEP 2 : GET RANDOM x Group and n Values

# In[6]:


group = 100
n = 50

sample = []
for i in np.arange(group):
    sample_sub = []
    for i in np.arange(n):
        sample_sub.append(polpulation.Weight[np.random.randint(0, N, 1)[0]])
    sample.append(sample_sub)


# In[9]:


mean_sample = np.mean([np.mean(x) for x in sample])
std_sample  = np.std([np.mean(x) for x in sample])

print('Mean of 100 sample is : ' + str(mean_sample))
print('Mean of 100 sample is : ' + str(std_sample))

print('Mean of Polpulation is : ' + str(X))
print('Mean of Polpulation is : ' + str(STD/np.sqrt(n)))


# ###  Kết luận
# Khi chọn ra n sample từ quần thể
# * Mean of Sample : 1 phân phối chuẩn, có giá trị trung bình sấp sỉ bằng với giá trị trung bình quản quần thể.
# * Standard Diviation : STD of Population / SQRT(N)

# In[ ]:


plt.plot(polpulation.groupby('Weight').count())
plt.axvline(x = X, linestyle = 'dashed', color = 'r', alpha = 0.4)
plt.axvline(x = mean_sample, linestyle = 'dashed', color = 'g', alpha = 0.4)
plt.ylabel('Mean of polpulation is : ' + str(X))
plt.xlabel('Mean of (Mean of each sample) is : ' + str(mean_sample))


# # 2. Point estimation
# 
# * Biết giá trị trung bình, phương sai của tổng thể. Xác định tỉ lệ xuất hiện của giá trị X

# ### STEP 1 : Tạo mẫu ngẫu nhiên cho Polpulation, có giá trị chiều cao.
# 
# * Mean of polpulation : 160
# * Std : 30

# In[ ]:


population = np.random.normal(loc = 160, scale=30, size = N).round()


# In[ ]:


population[0]

