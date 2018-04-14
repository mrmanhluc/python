
# coding: utf-8

# In[87]:


from __future__ import division
import nltk
import re
import pprint
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
nltk.download('punkt')
# URL link https://viblo.asia/p/xu-ly-ngon-ngu-tu-nhien-voi-python-p3-E375zy12lGW


# In[98]:


url = 'http://www.gutenberg.org/files/2554/2554-0.txt'
response = request.urlopen(url)
raw_data = response.read().decode('utf8')


# In[89]:


# Trong data có chứa những kí tự /n, /r .v.v
# Để xóa ký tự này, sử dụng word_tokenize

tokens = word_tokenize(raw_data)
print(tokens[:100])


# In[90]:


# Show data tokens dưới dạng Text
text = nltk.Text(tokens)
print(text)


# In[91]:


# Tìm kiếm, chỉ sử dụng cách này với data có size nhỏ

# Tìm đầu
search = raw_data.find('License')
print('Finded in rows : ',search)

# Tìm cuối
search = raw_data.rfind('License')
print('Founded in rows : ',search)


# In[96]:


# Xử lý data dạng HTML

url = 'http://news.bbc.co.uk/2/hi/health/2284783.stm'
html = request.urlopen(url).read().decode('utf-8')

tokens = word_tokenize(html)
print(tokens[:20])

# Xử dụng beatifulSoup load web
html = BeautifulSoup(html).get_text()
token = word_tokenize(html)
print(token[0:20])

