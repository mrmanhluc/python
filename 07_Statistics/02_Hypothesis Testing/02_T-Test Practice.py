
# coding: utf-8

# A research study was conducted to examine the differences between older and younger adults on perceived life satisfaction. A pilot study was conducted to examine this hypothesis. Ten older adults (over the age of 70) and ten younger adults (between 20 and 30) were give a life satisfaction test (known to have high reliability and validity). Scores on the measure range from 0 to 60 with high scores indicative of high life satisfaction; low scores indicative of low life satisfaction. The data are presented below. Compute the appropriate t-test.

# -- Bảng điều tra mức độ thỏa mãn về cuộc sống của 2 nhóm
# -- Nhóm 1 : Tuổi 20-30
# -- Nhóm 2 : Tuổi >30
# 
# -- Độ thỏa mãn từ : 0 - 60. Với 60 được xem là độ thỏa mãn cao nhất.

# In[33]:


import pandas as pd
import numpy as np
from scipy import stats


# In[34]:


# Data
older   = [45, 38, 52, 48, 25, 39, 51, 46, 55, 46]
younger = [34, 22, 15, 27, 37, 41, 24, 19, 26, 36]


# In[35]:


# Step 1: Tinh cac gia tri Means, Variance and Standard Deviation
data = pd.DataFrame([older, younger]).transpose()
data.rename(columns={0: 'older', 1:'younger'}, inplace=True)

print('Mean : ')
print(data.mean())

print('Varience : ')
print(data.var())

print('Standard Deviation')
print(data.std())


# In[36]:


# Step 2 : 

# 2.1 Ve biểu đồ phân bổ 2 Group
data.boxplot()


# ## Định nghĩa Hypothesis và Null Hypothesis
# 
# ### Hypothesis : Có mỗi liên hệ giữa độ tuổi và mức độ hài lòng cuộc sống
# ### Null hypothesis : Không có mỗi liên hệ giữa độ tuổi và mức độ hài lòng cuộc sống

# In[38]:


# Step 3: Check is normal distribute
stats.normaltest(data['older'])
stats.normaltest(data['younger'])


# In[42]:


# Step 4 : Tinh gia tri T-Test
stats.ttest_ind(older, younger)

