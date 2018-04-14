
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as pld


# In[118]:


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
    # Biến Static của Class (Biến của lớp) - Class's variable
    # self.name goi la atribute của class
    min_age, max_age = [10, 30]
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    


# In[119]:


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


# In[123]:


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

# Lưu ý : 
print(id(player2.min_age))
print(id(Player.min_age))
print(id(player1.min_age))


# In[137]:


class Animal:
    def __init__(self, name):
        # attribute la name
        self.name = name
    
    def showInfo(self):
        print ('Iam '+self.name)
        
    def move(self):
        print('Moving...')
        
class Cat(Animal):
    'Cat is class extends from Animal'
    
    def __init__(self, name, age, height):
        super().__init__(name)
        self.age = age
        self.height = height
        
    # Overight show_infor function
    def showInfo(self):
        print('Iam ' + self.name)
        print('Age : ', self.age)
        print('Height : ', self.height)
        
class Mouse(Animal):
    def __init__(self, name, age, hight):
        super().__init__(name)
        self.age = age
        self.hight = hight
        
    def showInfo(self):
        super().showInfo()
        print('Age : ', self.age)
        print('Heigh : ', self.hight)
        
    def move(self):
        print('Mouse moving..')


# In[139]:


tom = Cat('Tom Jerry', 18, 30)
tom.showInfo()

jerry = Mouse('Jerry', 5, 5)
jerry.showInfo()
jerry.move()


# In[140]:


# Class truu tuong. Abstract class
class AbstractDocument:
    def __init__(self, name):
        self.name = name
        
    def show(self):
        raise NotImplementedError('Subclass must implement abstract method')
    
class PDF(AbstractDocument):
    def show(self):
        print('Show PDF document :', self.name)
        
class Word(AbstractDocument):
    def show(self):
        print('Show word document :', self.name)


# In[143]:


documents = [PDF('PDF Document'), Word('Word Document')]

for doc in documents:
    doc.show()


# In[161]:


class Horse:
    maxHeight = 200
    
    def __init__(self, name, horse_hair):
        self.name = name
        self.horse_hair = horse_hair
        
    def run(self):
        print('Horse is run')
        
    def showName(self):
        print('Name : (Hourse of method ) : ', self.name)
    
    def showInfo(self):
        print('Horse Info')
        
class Donkey:
    def __init__(self, name, weight):
        self.name = name
        self.wight = weight
        
    def run(self):
        print('Donkey run')
        
    def showName(self):
        print('Name : (Donkey of method): ', self.name)
        
    def showInfo(self):
        print('Donkey info')
        
class Mule(Horse, Donkey):
    
    def __init__(self, name, hair, weight):
        Horse.__init__(self, name, hair)
        Donkey.__init__(self, name, weight)
    
    def run(self):
        print('Mule Run')
        
    def showInfo(self):
        print('-- Call Mule.showInfo')
        Horse.showInfo(self)
        Donkey.showInfo(self)


# In[180]:


print('Max Height :', Mule.maxHeight)
mule = Mule('Mule', 'Red',1000)

mule.run()

mule.showName()

mule.showInfo()

horse = Horse('Bach Ma', 'White')

issubclass(Mule, Mule)


# In[184]:


# Tinh da hinh trong Class

class English:
    def greeting(self):
        print('Hello')
        
class French:
    def greeting(self):
        print('Bonjour')
        
def intro(language):
    language.greeting()

flora = English()
aalase = French()

intro(aalase)

