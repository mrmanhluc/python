
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


plt.rcParams['font.family'] = 'Sans-serif' #全体のフォントを設定
plt.rcParams["figure.figsize"] = [20, 12]
plt.rcParams['font.size'] = 12 #フォントサイズを設定 default : 12
plt.rcParams['xtick.labelsize'] = 15 # 横軸のフォントサイズ
plt.rcParams['ytick.labelsize'] = 15


# In[4]:


# Loc : Giá trị Means mong muốn
# Weight of Male setting with 70 Kg.
N = 10000
Male   = {'mean' : 70, 'std': 10, 'N': N, 'colName' : ['Male'] *N}
Female = {'mean' : 60, 'std': 8,  'N': N, 'colName' : ['Female'] * N}

# Scale : Standard deviation
Male_weight = np.random.normal(loc = Male['mean'], scale = Male['std'], size = Male['N'])
Female_weight =np.random.normal(loc = Female['mean'], scale = Female['std'], size = Female['N'])


# In[5]:


People_weight = pd.concat([pd.DataFrame([Male_weight, Male['colName']]).transpose(), pd.DataFrame([Female_weight, Female['colName']]).transpose()])
People_weight.rename(columns={0 : 'Height', 1 : 'Sex'}, inplace= True)


# 
# 
# ## 1. Continue Values

# In[6]:


People_weight[9995: 10005]


# ### Mean cho Continue Values

# In[7]:


Mean_Male_01 = People_weight[People_weight['Sex'] =='Male'].Height.mean()
Mean_Male_02 = People_weight[People_weight['Sex'] =='Female'].Height.mean()

print([Mean_Male_02, Mean_Male_01])


# ## 2. Continue Values Type 1

# In[8]:


People_weight_Category = People_weight.pivot(index = People_weight.index, columns='Sex')['Height']
#https://stackoverflow.com/questions/26255671/pandas-column-values-to-columns

# Converted Data from Columns to Rows
People_weight_Category[0:10]


# In[9]:


People_weight_Category_01 = pd.DataFrame(np.transpose([[x for x in People_weight_Category['Male']], [y for y in People_weight_Category['Female']]]))
People_weight_Category_01.rename(columns={0 : 'Male', 1 : 'Female'}, inplace=True)
People_weight_Category_01.boxplot()


# ## Mean cho Continue Values
# 
# \begin{align}
# \bar{x} & = \frac{1}{N} \sum_{i=0}^{N} x_i
# \end{align}
# 

# In[10]:


# Means của 2 tập
People_weight_Category_01.mean()


# ### STANDARD DEVIATION - Continues Values
# 
# \begin{align}
# SD = \frac{1}{N - 1} \sum_{i=0}^{N} (x_i - \bar{x})^2
# \end{align}
# 

# In[11]:


# Standard Deviation
People_weight_Category_01.std()


# ## 3. Convert Data to Discrete Type

# In[12]:


group_male_counted = People_weight_Category_01.round().groupby(['Male']).count()
group_female_counted = People_weight_Category_01.round().groupby(['Female']).count()


# In[13]:


People_weight_discrete = pd.concat([group_male_counted, group_female_counted], axis=1)


# In[14]:


People_weight_discrete[30: 50]


# In[15]:


plt.plot(People_weight_discrete.index, People_weight_discrete['Male'], '-r')
plt.plot(People_weight_discrete.index, People_weight_discrete['Female'], '-b')
plt.xlabel('Weight')
plt.ylabel('Number')


# ## 3.1 Mean - Discrete Values
# 
# \begin{align}
# \bar{x} & = \sum_{i=10}^{n} x_i * P(x)
# \end{align}

# In[16]:


Mean_Female = pd.DataFrame(People_weight_discrete.index * People_weight_discrete.Female).sum()/People_weight_discrete.Female.sum()
Mean_Male = pd.DataFrame(People_weight_discrete.index * People_weight_discrete.Male).sum()/People_weight_discrete.Male.sum()


# In[17]:


plt.plot(People_weight_discrete.index, People_weight_discrete['Male'], '-r')
plt.plot(People_weight_discrete.index, People_weight_discrete['Female'], '-b')
plt.xlabel('Weight')
plt.ylabel('Number')
plt.axvline(x = float(Mean_Male), linestyle = 'dashed',  linewidth=2, color = 'r')
plt.axvline(x = float(Mean_Female), linestyle = 'dashed', linewidth=2, color = 'b')


# ## 3.2 Standard deviation and Variance

# \begin{align}
# SD = \frac{1}{N - 1} \sum_{i=0}^{N} (x_i - \bar{x})^2 * P(x)
# \end{align}
# 
# \begin{align}
# Var = \sqrt{SD}
# \end{align}

# In[18]:


Temp1 = pd.DataFrame(People_weight_discrete.Female.dropna().copy())
Temp2 = np.power(Temp1.index - float(Mean_Female), 2) * Temp1.Female

SD_Female = np.sum([x for x in Temp2])/ np.sum(Temp1.Female)
Var_Female = np.sqrt(SD_Female)

print('Standard deviation and variance of Female :')
print([SD_Female, Var_Female])


# In[19]:


Temp3 = pd.DataFrame(People_weight_discrete.Male.dropna().copy())
Temp4 = np.power(Temp3.index - float(Mean_Male), 2) * Temp3.Male

SD_Male = np.sum([x for x in Temp4])/ np.sum(Temp3.Male)
Var_Male = np.sqrt(SD_Male)

print('Standard deviation and variance of Male :')
print([SD_Male, Var_Male])


# In[20]:


fig, ax = plt.subplots()

plt.plot(People_weight_discrete.index, People_weight_discrete['Male'], '-r')
plt.plot(People_weight_discrete.index, People_weight_discrete['Female'], '-b')
plt.xlabel('Weight')
plt.ylabel('Number')
plt.axvline(x = float(Mean_Male), linestyle = 'dashed',  linewidth=2, color = 'r')
plt.axvline(x = float(Mean_Female), linestyle = 'dashed', linewidth=2, color = 'b')

# Define standard for Male of Region
standard_from_Male = Mean_Male - 2 * Var_Male
standard_to_Male = Mean_Male + 2 * Var_Male
ax.axvspan(int(standard_from_Male), int(standard_to_Male), alpha=0.4, facecolor='r')

# Define standard for Female of Region 
standard_from_Female = Mean_Female - 2 * Var_Female
standard_to_Female = Mean_Female + 2 * Var_Female

ax.axvspan(int(standard_from_Female), int(standard_to_Female), alpha = 0.4, facecolor='g')


# In[23]:


Mean_Male
Var_Male


# In[24]:


Mean_Male


# In[25]:


People_weight_discrete


# In[46]:


x = 40 #40 kg
(1/(np.sqrt(2*np.pi*SD_Male))) * np.exp(-(np.power(x-SD_Male, 2)/(2*Var_Male)))


# In[38]:


People_weight_discrete.Male[40] / np.sum(People_weight_discrete.Male)


# In[49]:


np.sum(People_weight_discrete.Male)


# In[40]:


People_weight_discrete.Male[40]


# In[48]:


SD_Male


# In[45]:


Male_weight.mean()

