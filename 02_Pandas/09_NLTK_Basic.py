
# coding: utf-8

# In[26]:


from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from nltk.book import *


# In[27]:


url = 'http://www.gutenberg.org/files/2554/2554-0.txt'

response = request.urlopen(url)
raw_data = response.read().decode('utf8')

type(raw_data)


# In[31]:


text1 = ' Moby Dick by Herman Melville 1851'
text2 = 'Sense and Sensibility by Jane Austen 1811'
text3 = 'The Book of Genesis'
text4 = 'Inaugural Address Corpus'
text5 = 'Chat Corpus'
text6 = 'Monty Python and the Holy Grail'
text7 = 'Wall Street Journal'
text8 = 'Personals Corpus'
text9 = 'The Man Who Was Thursday by G . K . Chesterton 1908'


# In[33]:


text9.concordance('Was')

