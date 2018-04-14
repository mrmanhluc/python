
# coding: utf-8

# In[5]:


from bs4 import BeautifulSoup
from urllib import request


# In[11]:


url = r'http://faq.lixil.co.jp/?site_domain=default'
html = request.urlopen(url).read().decode('utf8')

raw_data = BeautifulSoup(html).get_text()
raw_data

# Delete kí tự \n\r\ không cần thiết

tekens = word_tokenize(raw_data)

