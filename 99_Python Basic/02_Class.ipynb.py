
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as pld


# In[93]:


class Rectangle:
    'This is Rectangle class'
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getArea(self):
        return self.width * self.height

class Persion:
    'This class is save about persion information'
    
    def __init__(self, name, age, gender = 'Male'):
        self.name = name
        self.age = age
        self.gender = gender
        
    def showInfor(self):
        print('Name : ', self.name)
        print('Age : ',self.age)
        print('Gendee : ', self.gender)

class Player:
    'This is player function'
    
    min_age, max_age = [10, 30]
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    


# In[94]:


r1 = Rectangle(10, 15)
r2 = Rectangle(20, 11)

r1.getArea()
r2.getArea()

persion1 = Persion('Luc', 39)
persion1.showInfor()

persion2 = persion1
persion2.name = 'Tuan'

# Persion2 la con tro tro toi persion 1
# khi persion 2 thay doi, gia tri cua persion 1 cung thay doi
persion2.showInfor()
persion1.showInfor()

persion1 == persion2


# In[107]:


# Test attribute player
player1 = Player('Luc', 20)
player2 = Player('Thu', 15)

player2.age = 30
player2.address = 'Khu pho 3 thi tran yen cat'

player2.address

#Cach truy cap toi attribute bang cach khac thay vi dau .
# Thay vi player2.address, co the thay bang ham getattr
getattr(player2, 'address')

# Kiem tra doi tuong co Attribute hay khong
# player 2 co chua attribute 'adress', ket qua tra ve la true
hasattr(player2, 'address')

# player 1 khong chua attribute 'Address', ket qua tra ve false
hasattr(player1, 'address')

# Set gia tri cho attribute, neu attribute khong ton tai thi tao ra
setattr(player1, 'address', 'Cho Lach, Ben Tre')
getattr(player1, 'address')
hasattr(player1, 'address')

player1.min_age = 30
player1.min_age

player2.min_age
player1.min_age

Player.min_age = 40

player1.min_age 

dỉ

