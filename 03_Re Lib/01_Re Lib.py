
# coding: utf-8

#  Re Code				|   Means
#  -----------------------|----------------------------------------------
#  [1-9]					|	Select toàn bộ số
#  [-Z]					|	Select toàn bộ kí tự từ A-Z
#  [^1-9]					|	Chọn tất cả, ngoại trừ 1-9
#  [^1-9, ^a-z, ^A-Z]		|	Chọn tất cả ngoại trừ 1-9, a-z, A-Z
#  \d\d\d					|	Tìm kiếm số có 3 chữ số bất kì
#  \D						|	Chọn tất cả 
#  \s						|	Tìm kiếm khoảng trắng
#  \S						|	Tất cả khoảng không phải space
#  .*						|	Tất cả kí tự phía sau
#  *.						|	Tất cả kí tự phía trước
#  x.*.z					|	Lấy tất cả kí tự nằm trong khoảng từ x-z
#  x.*.z,\d\d				|	Lấy tất cả kí tự từ x-z và thêm 2 giá trị số đứng sau
#  \w : 					|	Toàn bộ kí tự
#  \w+ : 					|	Toàn bộ câu, phân biệt bởi dấu space hoặc các dấu không phải kí tự
#  ^  					|	Vị trí bắt đầu, $ Vị trí kết thúc
# \|'						|	Phep hoac
#  [A-Z]{6} 				|	6 kí tự bất kì từ A-Z
# $ 						|	Kết thúc chuỗi

# In[1]:


import re
# from bs4 import BeautifulSoup


# In[13]:


# url = 'http://www.lixil.co.jp/showroom/qa/'
# ask_ans = BeautifulSoup(url).getText()
# ask_ans


# In[56]:


# Findall . Tìm chính xác

text = "guru99, education is fun google too fun"
r1 = re.findall(r'^\w+',text)

# Find từ đầu tới khi gặp 2 chứ số \d\d 
r2 = re.findall(r'.*\d\d', text)
r2
print(r2)

# Find từ education tới hêt
r3 = re.findall(r'education.*', text)
print(r3)

# Find toàn bộ câu trong đonạ text
r3 = re.findall(r'\w+', text)
print(r3)

# Find toàn bộ câu bắt đầu bằng chữ g. Ví dụ google, guru
r4 = re.findall(r'g\w+', text)
print(r4)


# In[11]:


text2 = 'split the words'
print(re.split(r'\', text2))


# In[83]:


# re.match

list = ['guru99 get', 'guru99 give', 'guru Selenium']

for lst in list:
    z = re.match(r'(g\w+)\W(g\w+)', lst)
    if z: 
        print(z.groups())


# In[84]:


# re.search

patterns = ['Software testing', 'guru99']
text = 'Software testing is fun'

for pt in patterns:
    print('\nLooking for "%s" in "%s" ->' %(patterns, text) , end = '')


# In[85]:


temp = 'guru99 get this is gooole is for good'
z = re.match(r'(g\w+)', temp)

if z:
    print(z.groups())
    
z = re.findall(r'g\w+', temp)
print(z)


# In[186]:


# Phân biệt giữa match và find
# Match sử dụng để tìm chuỗi yêu cầu đúng định dạng, format

# Match đưuọc sử dụng để validate format của toàn bộ text

# Với việc findall, nó sẽ tìm kiếm đoạn
# fake@mrmanhluc@gmail.com
# Thấy đoạn mrmanhluc@gmail.com thỏa mãn yêu cầu

# Còn Match, toàn bộ đoạn face@mrmanhluc@gmail.com sẽ đưuọc xem xét
# Nếu không phù hợp sẽ bị loại bỏ

# Bài toán 1. Tìm kiếm email trong 1 danh sách.
# Sử dụng Find

# Bài toán 2. Kiểm tra các email cso hợp với format hay không
# Sử dụng match

email = 'mrmanhluc@gmail.com, djaskdjiasjdi, levanluong@gmail.com'
fake_email = 'fake@mrmanhluc@gmail.com'

fake_email1 = 'mrmanhluc@gmail.com@fakeMail@gmail.com'

regex = r'[A-Z,a-z,0-9]+@gmail.com'

z1 = re.match(regex, fake_email)
z2 = re.match(regex, fake_email1)

# z2 = re.findall(regex, fake_email1)

print(z2)


# In[237]:


# Yêu cầu : đọc vào tập các file name, kiểm tra file name có đúng định dạng hay không
# In ra tập danh sách phù hợp với Format.
# Bắt đầu là kí tự từ a-z. [a-z] 
# Kết thúc bằng .txt $

regex = r'([a-z]+(00)+[1-9]+(.txt)$)'

fileName = ['001file001.txt','file0013.txt', 'file001.txt', 'file002.txt', 'file003.txt.zip', 'file01_01.txt', 'file01_02.txt']

for file in fileName:
    z = re.fullmatch(regex, file)
    if z:
        print(z.group())
        
        
regex1 = r'^\d'

z = re.match(regex1, '0inchao')
if z:
    print(z)


# In[246]:


# So sánh Math sẽ được so sánh từ đầu trái của string

txt = 'Xin chao, hello'

z = re.match('Xin chao', txt)

print(z.groups)
#z = re.match('.*hello', txt)
#print(z)


# In[248]:


# So sánh fullmath sẽ đưuọc so sánh toàn bộ string
txt = 'Xin chao, hello'

z = re.fullmatch('Xin chao, hello',txt)
print(z)


# In[260]:


# Find all
txt = 'Xin chao, hello xin chao'

z = re.findall('in', txt)
print(z)


# In[262]:


# Tìm khớp và Repace
txt = 'Xin chao, hello toi la luc'

re.sub('Xin', 'xin', txt)


# In[1]:


[False]*3


# In[2]:


3 in [2, 3, 4]


# In[13]:


x = range(10, 19)
True & (int('1') in range(1, 13))


# In[30]:


temp = '12-A6'
print(temp)
re.findall(r'\d\d-[A-Z][0-9]', temp)


# In[32]:


str(True).lower()


# In[51]:


txt = 'abc123abc'
txt1 = '123234'
input_txt = '2018/03/03 03:02'

def is_date(in_data):
    # Kiểm tra có phải là số không
    re.match(r'^[0-9]+$', txt1)

    # Kiểm tra str có phải dạng datetime không
    pattern1 = r'^\d\d\d\d/\d\d/\d\d$'
    pattern2 = r'^\d\d\/\d\d/\d\d$'
    pattern3 = r'^\d\d\d\d\/\d\d\/\d\d \d\d\:\d\d$'
    pattern4 = r'^\d\d\/\d\d\/\d\d \d\d\:\d\d$'
    pattern = [pattern1, pattern2, pattern3, pattern4]

    for pt in parterm:
        if re.match(pt, in_data) is not None:
            return True
    return False

def is_num(in_data):
    return in_data.replace('.','',1).isdigit()

def get_dataType(in_data):
    if (is_date(in_data)):
        return 

# re.findall(r'^a.*', txt1)


# In[108]:


date


# In[107]:


'3123123121214'.replace('.','',1).isdigit()

