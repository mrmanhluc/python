
# coding: utf-8

# ### Bài toán thực tế.
# 
# Công ty samsung nhận nhiều khiếu nại về việc Pin của họ gặp lỗi khiến máy nóng hơn so với bình thường.
# 
# Theo tính toán, nhiệt độ trung bình đạt tiêu chuẩn là 30 độ.
# 
# Theo luật, công ty phải thu hồi toàn bộ sản phẩm đã bán nếu nhiệt độ trung bình của  (95% số lượng) có nhiệt độ trung bình > 5% nhiệt độ tiêu chuẩn.
# 
# Các bước mà công ty samsung tiến hành điều tra về tình trạng về số lượng sản phẩm gặp phải như sau.
# 
# H0 : Máy có nhiệt độ trung bình > 30 độ.
# H1 : Máy có nhiệt độ trung bình <= 30 độ

# ### Step 1 : 
# Thu thập ngẫu nhiên 70 sản phẩm, đo nhiệt độ trung bình của 70 sản phẩm trên.

# In[15]:


import pandas as pd
import numpy as np
import matplotlib as plt
from scipy import stats as sts


# In[22]:


# Tạo array ngẫu nhiên, với means của mẫu = 30, Scale : Standard Divition (độ lệch chẩun) = 5 và số phần từ 70
m = 28
x_bar = 30
N = 70
sd = 5

data = np.random.normal(loc=m, scale= sd, size = N)


# In[23]:


pd.DataFrame(data).boxplot()


# In[24]:


sts.ttest_1samp(data, 0.05)


# In[42]:


temp = (m - x_bar) / (np.std(data) / np.sqrt(N))


# In[43]:


temp


# In[39]:


sts.ttest_1samp(data, 10)

