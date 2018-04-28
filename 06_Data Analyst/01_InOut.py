
# coding: utf-8

# In[2]:


import pandas as pd
import re
import os.path
import codecs as cd
import glob  


# In[4]:


class inputFile:
    ''
        
    def get_Extension(url):
        return os.path.splitext(url)[1]
    
class read_csv:
    ''
    
    # Read file into self
    def __init__(self, url):
        with cd.open(url, "r", "Shift-JIS", "ignore") as csv_file:
            self.df = pd.read_table(csv_file, sep=',')
            
    # Get file with Pandas Data Type
    def readfile(self):
        return self.df
    
    # Show top n rows
    def show_top(self, n):
        return self.df[0: n]
    
    # Get columns name
    def get_colName(self):
        return self.df.columns


# In[5]:


URL = r'D:\01_Project\Lixil Analysis\input\data\faq.csv'

# inputFile.get_Extension(URL)

file = read_csv(URL)


# In[6]:


file.get_colName()


# In[7]:


file.columns


# In[21]:


URL1 = r'D:\01_Project\Lixil Analysis\input\data\*.csv'
files = glob.glob(URL1)
for fn in files:  
    print(type((str.split(fn, '\\')[-1:])[0]))

