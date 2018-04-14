
# coding: utf-8

# In[292]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, date


# In[293]:


# I. Create database
col_name = ['studentId','classId','Name','Sex','BirthDay', 'Mark']
student_num = 100
student_id = []
class_id = []
birthday = []
Name = []

for x in range(student_num):
    student_id.append('S' + np.str(x))

class_id = []
for x in range(student_num):
    class_id.append('class' + np.str(np.random.randint(1,4,1)[0]))

# Create random name
firt_name = ['Nguyen', 'Tran', 'Do', 'Le', 'Luong']
mid_name = ['Van', 'Thi', 'Thanh', 'Quynh', 'Lai']
last_name = ['Kiet', 'Tam', 'Luc', 'Nam', 'Hong', 'Tuan', 'Hai', 'Hoa']

for x in range(student_num):
    Name.append(firt_name[np.random.randint(0, len(firt_name))] + ' ' + mid_name[np.random.randint(0,len(mid_name))] + ' ' + last_name[np.random.randint(0,len(last_name))] )
    
Sex = np.random.randint(0, 2, student_num)
Sex = list(map(lambda x: ['Nu', 'Nam'][x], Sex))

# Create data for Birthday
for x in range(100):
    birthday.append(pd.Timestamp(np.random.randint(1980, 1999),np.random.randint(1,12), np.random.randint(1,28)))

# Random mark of student
Mark = np.random.randint(1,10, 100)
Mark

# Create dataFrame for Student information
len(birthday)


# In[294]:


dataFrame = pd.DataFrame({
    'Name': Name,
    'Student Id' : student_id,
    'Mark' : Mark,
    'Sex' : Sex,
    'Birthday' : birthday,
    'Mark' : Mark,
    'Class' : class_id
})

dataFrame.head(5)


# In[299]:


# List of student Sex is Nu
dataFrame[dataFrame.Sex == 'Nu']

# List of student Sex is Nu and Mark > 8
dataFrame[((dataFrame.Sex == 'Nu') & (dataFrame.Mark> 8))]

# Calculator Age from Birthday
def calculate_age(born):
    return date.today() - born.year

dataFrame["Age"] = pd.to_datetime(
    dataFrame.Birthday
dataFrame


# In[141]:


# list(map(lambda y: 'str' + str(y), range(100)))


# In[323]:


for x in range(100):
    pd.Timestamp(np.random.randint(1980, 1999),np.random.randint(1,12), np.random.randint(1,31))


# In[326]:


(datetime.now() - dataFrame.Birthday)

