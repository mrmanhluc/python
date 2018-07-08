
# coding: utf-8

# # Kiểm định - Hypothesis Testing

# ### input data : 
# * Độ tuổi trung bình người dân, Sample N = 1000 Values.
# * Mean of Population = 67
# * Std = 3.1
# 
# ### Hypothethis : 
# * H0 : Độ tuổi trung bình người dân là 67 tuổi
# * H1 : Độ tuổi trung bình > 67 tuổi
# 
# ### Z-Test
# * Chuyển về phân phối Standard Normal Distribution

# In[22]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[30]:


N = 1000
sample_test = pd.DataFrame(np.random.normal(loc = 68, scale=3, size=N).round(), columns=['Age'])


# In[31]:


sample_test.hist()


# In[38]:


mean_sample = sample_test.mean()
std_population = 3
mean_population = 67


# In[41]:


Z = (mean_sample - mean_population) / (std_population / np.sqrt(N))


# In[43]:


# Xác định với mức ý nghĩa Alpha = 0.05, có thể bác bỏ giả thiết H0 hay không?


# In[44]:


Z>1.645


# ### Chứng minh giả thiết

# ## STEP 1 :
# * Tạo Data Random cho Polpulation, có độ tuổi trung bình 67, độ lệch chuẩn 3, số lượng người trong toàn bộ quần thể 10000

# In[252]:


population = pd.DataFrame(np.random.normal(loc = 67, scale= 10, size = N*10).round(), columns=['Age'])


# In[253]:


population.plot.hist()


# In[254]:


population[0:30]


# ## STEP 2 : 
# * Select random 100 người từ quần thể trên

# In[294]:


n = 100
temp = {1}

mean_sample = 0
random_sample = []

while (mean_sample <= 68 or mean_sample>=66):
    temp = {1}
    ## Get random difirence n value
    while(len(temp) != 100):
        temp.add(np.random.randint(0, 10000, 1)[0])

        random_i = []
    for i in temp:
        random_i.append(i)
    random_sample = [population.Age[x] for x in random_i]
    mean_sample = np.mean(random_sample)
    print(mean_sample)
random_sample = pd.DataFrame(random_sample, columns=['Age'])


# In[291]:


random_sample


# In[285]:


population_temp = population.copy()
population_temp['temp'] = len(population) * [1]

plt.plot(population_temp.groupby('Age').count())
plt.axvline(x = mean_sample, linestyle = 'dashed',  linewidth=2, color = 'r')

