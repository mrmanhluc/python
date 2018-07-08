
# coding: utf-8

# In[16]:


import numpy as np
from scipy import stats
import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

plotly.tools.set_credentials_file(username='mrmanhluc', api_key='GGyYOj3zaR8fwdxCjWAO')


# In[17]:


# Step 1 : Tạo 2 tập a và b ngẫu nhiên

# Cỡ mẫu - Sample Size
N = 10

# Tạo 1 phân phối Gaussian Distribute 
# Mean = 2. Var = 1 (Trung bình : 2, độ lệch chuẩn : 1)
a = np.random.normal(0, 1, size = N)

# Mean = 0. Var = 1
b = np.random.normal(2, 1, size = N)


# In[18]:


pd.DataFrame([a,b]).transpose().boxplot()


# In[28]:


x = np.linspace(-4, 4, 160)
y1 = stats.norm.pdf(x)
y2 = stats.norm.pdf(x, loc = 2)

trace1 = go.Scatter(
    x = x,
    y = y1,
    mode = 'lines+markers',
    name = 'Mean of 0'
)

trace2 = go.Scatter(
    x = x,
    y = y2,
    mode = 'lines+makers',
    name = 'mean of 2'
)

data = [trace1, trace2]

py.iplot(data, filename= 'normal-dist-plot')


# In[29]:


data1 = np.random.normal(0,1, size = 50)
data2 = np.random.normal(2,1, size = 50)

true_mu = 0

onesample_results = stats.ttest_1samp(data1, true_mu)

maxtrix_onesample = [
    ['', 'Test Statistic', 'p-value'],
    ['Sample Data', onesample_results[0], onesample_results[1]]
]

onesample_table = FF.create_table(maxtrix_onesample, index = True)

py.iplot(onesample_table, filename = 'onesample-table')


# In[ ]:


pd.DataFrame([a,b]).transpose().plot


# In[22]:


# Step 2 : Tính độ lệch chuẩn Standard Deviation

# Step 2.1 Phương sai, với bậc tự do  = 1

var_a = a.var(ddof = 1)
var_b = b.var(ddof = 1)

s = np.sqrt((var_a + var_b)/2)
s


# In[25]:


# Step 3. Tinhs T-Statistics

t = (a.mean() - b.mean())/(np.sqrt((var_a + var_b)/(N)))

t1 = (a.mean() - b.mean())/(s * np.sqrt(2/N))
t


# In[26]:


# Step 4. Tính độ tự do Degress of freedom
df = 2 * N - 2

p = 1 - stats.t.cdf(t, df = df)

print("t = "+ str(t))
print("p = "+ str(2 * p))


# In[28]:


# Step 5 : Tính giá trị T-test theo Function stats

t2, p2 = stats.ttest_ind(a, b)
print("t = "+str(t2))
print("p = "+str(2*p2))

