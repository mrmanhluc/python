
# coding: utf-8

# In[1]:


import numpy as np


# In[10]:


string = 'nguyen manh luc'

# IN hoa chu cai dau tien
string.capitalize()

string.center(100, '#')


# In[13]:


# Đếm kí tự xuất hiện trong chuối
string.count('n')


# In[28]:


str1 = 'Nguyễn Mạnh Lực'
str2 = 'グエン・マン・ルック'
temp = str2.encode('utf-8')


# In[33]:


temp2 = temp.decode('utf-8')
temp2


# In[34]:


temp


# In[40]:


# Kiểm tra kết thúc bằng một kí tự
str2.endswith('マン・ルック')
# Có thể kiểm tra được 1 hoặc chuỗi kí tự


# In[46]:


# Thay thế Tabs \t bằng khoảng trắng

print(str1)


# In[47]:


#thay thế 1 Tab = 1 space
str1.expandtabs(1)


# In[9]:


# Tim kiem : Trả về vị trí đầu tiên khi tìm thấy chữu Manh
str1 = 'Nguyễn\tManh\tLuc\tManh'
str1.find('Manh')

# Rfind() : Trả  về vị trí cuối cùng mà tìm được chuỗi
print(str1.rfind('Manh'))


# In[10]:


# Index (Như hàm find, tuy nhiên sẽ gọi Exception khi khôn tim thấy)
str1 = 'Nguyễn\tManh\tLuc\tManh Luc'
print(str1.index('Luc'))
# Exception bao not founded
print(str1.rindex('Luc'))


# In[11]:


# Check chuỗi có chứa số hay không?

str1 = r'123123dkaosdkoあ'

print(list(str1)[len(str1)-1].isalnum())

str2 = '12334dasdas578'

print(str2.isalnum())

print(str2.isdigit())

temp = 0
# Kiểm tra string có phải chứa duy nhất số hay không
print(str1, str1.isdigit())

if str2.isdigit():
    temp = (int)(str2)
    
# Kiếm tra số, chữ 
print(str1,str1.isdecimal())

print(str2, str2.isdecimal())

# Kiếm tra chuỗi bao gồm cả chữ và số
print(str1, str1.isalnum())

str3 = 'ádasdas123pl'
print(str3, str3.isalnum())


# In[12]:


# Kiểm tra in thường
str1 = 'ABC'
print(str1.islower())

str2 = 'abc'
print(str2.islower())

# Kiểm tra in hoa
print(str1.isupper())


# In[13]:


# isnumeric và isdigint
x1 = '12345123'
x2 = 'abc123'

print(x1.isnumeric())
print(x2.isnumeric())
print(x1.isdigit())
print(x2.isdigit())


# In[14]:


# Kiếm tra 1 chuỗi chỉ chứa duy nhất space
x1 = '    '
x2 = ' asd đá'

print(x1.isspace())
print(x2.isspace())


# In[15]:


# Chuỗi Title là chuỗi có chữ cái đầu in hoa
title1 = 'This Is Title'
title2 = 'This is Not Title'

print(title1.istitle())
print(title2.istitle())

# Convert 1 chuỗi sang Title : In hoa các chữ cái đứng đầu
title3 = 'nguyen manh luc'
print(title3.title())

# Swapcase . Hoa -> Thường, Thường -> Hoa
print(title2.swapcase())


# In[16]:


# Join string
str_one = 'LUC NGUYEN'
str_two = '**..'
print(str_one.join(str_two))

# Len
print(str_one)
print(list(str_one))

print(len(str_one))
print(len(list(str_one)))


# In[29]:


# Print string với len cho xác định trước
str1 = '123'

# TÌnh huống len quá dài
print(str.ljust(20, '-'))

# Tình huống len quá ngắn
print(str.ljust(2, '-'))

# Bù phải
print(str.rjust(30, '-'))

# Thêm kí tự 0 cho đủ độ dài

student_id1 = '9'
student_id2 = '10'

print('Student 9 Id is',student_id1.zfill(3))
print('Student10 Id is',student_id2.zfill(3))


# In[18]:


# Convert
# Convert to lower

str1 = 'Nguyen manh luc'
print(str1.upper())

print(str1.lower())


# In[19]:


# Loại bỏ kí tự char đầu chuỗi

# lstrip() mặc định input là ' ' 
str2 = '   Nguyen Manh Luc'
print(str2.lstrip())

str3 = 'Nguyen Manh Luc'
print(str3.lstrip('N'))

# Lọa n kí tự nếu n kí tự đầu giống nhau
str4 = 'NNnguyenmanh Luc'
print(str4.lstrip('N'))

# Có phân biệt chữ hoa và thường
print(str3.lstrip('n'))

str5 = '\tNguyen Manh Luc\n'
print(str5)

# Loại bỏ tab đầu dòng
print(str5.lstrip('\t'))


# In[20]:


str5 = '\tNguyen Manh Luc\n'

print(str5)
#Loại bỏ xuống dòng
print(str5.rstrip('\n'))


# In[21]:


#Loại bỏ kí tự ở 2 đầu chuỗi
str5 = '\tNguyen Manh Luc\n'

print(str5.strip('\t'))
print(str5.strip('\n'))


# In[155]:


# Replace
str1 = 'ABC Rep XYZ Rep'
print(str1.replace('Rep', 'KLM'))

# 1 : giới hạn số từ đưuọc thay để
print(str1.replace('Rep', 'KLM', 1))


# In[158]:


# Max : Tìm chữ có vị trí 
str1 = 'ABCabcXyzXyZ'

print(max(str1))
print(min(str1))


# In[188]:


# Split cắt
str1 = 'Nguyen,manh,luc'
print(str1.split(','))

# Split giới hạn số lượng
print(str1.split(',', 1))

# Split chuỗi bằng \n
str2 = 'rows1\nrows2\nrows3'
print(str2)
print(str2.splitlines(3))


# In[191]:


# Kiểm tra kí tự đầu tiên first có bắt đầu bằng....

id1 = 'id001'
id2 = '002'

print('id1 start with id check :', id1.startswith('id'))

print('id2 strat with id check : ', id2.startswith('id'))


# In[203]:


# Translate cho chuoi
inputs = 'Toi la'
outs = '私は'

outs = outs.ljust(len(inputs), ' ')
str1 = 'Toi la Luc'
trans = str1.maketrans(inputs, outs)

trans = trans.repl
print(str1.translate(trans))


# In[35]:


# del str
str(3).rjust(5, '0')


# In[30]:


# Thêm giá trị 0 vào int
'{0:0>3}'.format(999)

