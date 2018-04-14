
# coding: utf-8

# In[15]:


# Exception can ban
d = 0
try : 
    value = 10/d
    print('Values is ',value)
except ZeroDivisionError as e:
    print('Error : ',str(e))
    print('Ignore to continue..')
    


# In[16]:


# Xu ly check tuoi, voi class duoc thua ke tu Exception

class AgeException(Exception):
    def __init__(self, msg, age):
        super().__init__(msg)
        self.age = age
        
class TooYoungException(AgeException):
    def __init__(self, msg, age):
        super().__init__(msg, age)
        
class TooOldException(AgeException):
    def __init__(self, msg, age):
        super().__init__(msg, age)
        
def checkAge(age):
    if(age < 18):
        raise TooYoungException('Age' + str(age) + 'Too Young', age)
    
    elif(age > 40):
        raise TooOldException('Age' + str(age) + 'Too Old', age)
    
    print('Age' + str('age') + 'Oke')


# In[17]:


age = 90

try:
    checkAge(age)
    print('you pass')
except TooYoungException as e:
    print('You are too young, not pass')
    print('Couse Messege :', str(e))
    print('Invalid age : ',e.age)
    
except TooOldException as e:
    print('You are too old, not pass')
    print('Cause Message : ', str(e))
    print('Invalid age : ', e.age)

