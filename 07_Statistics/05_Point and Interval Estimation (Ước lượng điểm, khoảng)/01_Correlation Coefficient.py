
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statistics import mode


# In[82]:


plt.rcParams['font.family'] = 'Sans-serif' #全体のフォントを設定
plt.rcParams["figure.figsize"] = [20, 12]
plt.rcParams['font.size'] = 12 #フォントサイズを設定 default : 12
plt.rcParams['xtick.labelsize'] = 15 # 横軸のフォントサイズ
plt.rcParams['ytick.labelsize'] = 15


# ## Correlation Coeffienct - Khoảng tin cậy
# 
# Cho tập Polpulation bất kì, lấy ngẫu nhiên n Sample bất kì từ Polpulation đó, tính toán khoảng tin cậy của giá trị trung bình dựa vào Sample đã cho

# ## STEP 1
# Create Polpulation with N = 10000 member

# In[20]:


N = 10000


# In[117]:


population = pd.DataFrame(np.random.randint(5, 100, size = N), columns=['weight'])
population['temp'] = N * [1]

mean_population = population.weight.mean()
std_population = population.weight.std()

population[0:10]


# ## STEP 2
# Lấy ra 100 Sample bất kì từ Population trên. 
# Mỗi Sample chứa 50 giá trị.
# 
# Sử dụng phương pháp lấy mẫu không hoàn lại

# In[27]:


sample_num = 100
sample_member_num = 50
sample = []

def random_not_return(min_location, max_location, number):
    '''
    Tạo ngẫu nhiên n vị trí không trùng nhau
    min_location : Lấy từ min 
    min_location : Lấy tới vị trí max
    number : Số vị trí sẽ sinh ra
    '''
    
    location_dic = {1}
    location_arr = []
    while(len(location_dic) < number):
        location_dic.add(np.random.randint(low = min_location,high= max_location, size=1)[0])
    for x in location_dic:
        location_arr.append(x)
    return location_arr

def random_value(sam_num, member_num):
    '''
    Lấy ngẫu nhiên n sample. Mỗi sample có chứa m phần từ
    sam_num : Số sample muốn lấy ngẫu nhiên
    member_num : Số lượng member chứa trong mỗi sample
    
    '''
    sample_arr = []
    
    for i in np.arange(sam_num):
        local = random_not_return(0, N, member_num)
        sample_arr.append([population.weight[x] for x in local])
        
    return sample_arr
    
def get_mean_sample(sample_arr):
    mean_sam = []
    
    for arr in sample_arr:
        mean_sam.append(np.mean(arr))
    return mean_sam

def get_mode_sample(sample_arr):
    count = 0
    sample_arr = pd.DataFrame(sample_arr, columns=['values'])
    sample_arr['temp'] = len(sample_arr) * [1]
    sample_arr = pd.DataFrame(sample_arr.groupby('values').count())
    sample_arr[]

sample = random_value(sample_num, sample_member_num)
mean_sample = get_mean_sample(sample)


# In[198]:


fig = plt.figure(2, figsize=(20, 10))
ax = fig.add_subplot(111)
bp = ax.boxplot(sample[0:50], showmeans=True, showcaps=True)
ax.plot([0, 50], [mean_population-1,mean_population-1], 'r--', lw=3)
ax.plot([0, 50], [np.mean(mean_sample),np.mean(mean_sample)], 'g--', lw=3)

ax.plot([0, 50], [std_population/np.sqrt(sample_member_num),std_population/np.sqrt(sample_member_num)], 'r-', lw=1)


# * Red line : Mean of Population

# ## Kết luận 1
# * Khi lấy 1 Sample bất kì từ Population, giá trị trung bình của Population luôn luôn nằm trong khoảng tin cậy của Sample đó.
# 
# Đơn giản mà nói, hỏi 100 nhóm bất kì, tối thiểu có tới 95 nhóm có người nặng 51.87Kg(Trung bình quần thể).
# Đây là định lý giới hạn trung tâm

# ## STEP 3
# Tính khoảng tinh cậy cho N Sample

# In[185]:


n_rows = 5
n_cols = 10
for i in np.arange(n_rows * n_cols):
    plt.subplot(n_rows, n_cols, i+1)
    plt.hist(sample[i+1])



#plt.subplot(n_rows, n_cols, i+1)
#plt.hist(sample[i+1])

#plt.subplot(n_rows, n_cols, i+2)
#plt.hist(sample[i+2])


# In[190]:


def standardize(sample_arr):
    sam_mean = np.mean(sample_arr)
    sam_std = np.std(sample_arr)
    z_standardize = [(x-sam_mean)/(sam_std) for x in sample_arr]
    return z_standardize

sample_standardize = [standardize(x) for x in sample]


# In[192]:


n_rows = 5
n_cols = 10
for i in np.arange(n_rows * n_cols):
    plt.subplot(n_rows, n_cols, i+1)
    plt.hist(sample_standardize[i+1])

