
# coding: utf-8

# In[3]:


from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
from urllib import request


# In[10]:


url = 'http://www.gutenberg.org/files/2554/2554-0.txt'

response = request.urlopen(url)
raw_data = response.read().decode('utf8')

type(raw_data)

