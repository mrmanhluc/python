
# coding: utf-8

# In[51]:


import math
import re
from operator import itemgetter, attrgetter


# # Bài 01: 
# Câu hỏi: Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.

# In[ ]:


arr = []
for i in range(2006, 3201, 7):
    if i % 5 != 0:
        arr.append(str(i))
        
print(', '.join(arr))


# ## Bài 02: 
# 
# Câu hỏi: 
# 
# Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

# In[ ]:


x = int(input('Enter values'))

def fact_1(x):
    gt = 1
    for i in range(x):
        gt *= (i + 1)
    return str(gt)

# De quy
def fact_2(x):
    if x == 0:
        return 1
    return x * fact_2(x-1)

print(fact_2(x))


# ## Bài 03: 
# 
# Câu hỏi: 
# 
# Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i) như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này. Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.

# In[ ]:


n = int(input('Enter n value'))

# Cách ngu
keys = []
values = []
for i in range(1, n+1):
    keys.append(i)
    values.append(i**2)
key_value = zip(keys, values)

dic = dict(key_value)

# Cách khôn
dic1 = dict()
for i in range(1, n+1):
    dic1[i]=i*i
    
print(dic1)

# Note : Bản chất của dict cũng chỉ là array có chứa Index thay vì chứa thứ tự phần tử


# ## Bài 04:
# 
# Câu hỏi:
# 
# Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển, tạo ra một danh sách và một tuple chứa mọi số.
# 
# Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
# 
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# 
# Gợi ý: 
# 
# Viết lệnh yêu cầu nhập vào các giá trị sau đó dùng quy tắc chuyển đổi kiểu dữ liệu để hoàn tất.

# In[ ]:


values_in = str(input('Enter Values: ')).trim()

values_in = values_in.split(',')
convert_totuple = tuple(values_in)

print(values_in, convert_totuple)


# ## Bài 05:
# 
# Câu hỏi:
# 
# Định nghĩa một class có ít nhất 2 method: 
# 
# getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
# 
# printString: in chuỗi vừa nhập sang chữ hoa. 
# 
# Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.
# 
# Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM

# In[ ]:


class InputOutString(object):
    def __init__(self):
        self.in_value = ''
        
    def getString(self):
        input_value = input('Enter s values: ')
        self.in_value = input_value
        
    def printString(self):
        print(str.upper(self.in_value))
    
str1 = getsetString()
str1.getString()
str1.printString()


# ## Bài 6:
# 
# Câu hỏi:
# 
# Viết một method tính giá trị bình phương của một số.
# 
# Gợi ý: 
# 
# Sử dụng toán tử **.
# 
# 

# In[ ]:


a = int(input('Enter values'))
print(a**2)


# ## Bài 7: 
# 
# Câu hỏi:
# 
# Python có nhiều hàm được tích hợp sẵn, nếu không biết cách sử dụng nó, bạn có thể đọc tài liệu trực tuyến hoặc tìm vài cuốn sách. Nhưng Python cũng có sẵn tài liệu về hàm cho mọi hàm tích hợp trong Python. Yêu cầu của bài tập này là viết một chương trình để in tài liệu về một số hàm Python được tích hợp sẵn như abs(), int(), input() và thêm tài liệu cho hàm bạn tự định nghĩa.

# In[ ]:


print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)

def square(x):
    """Create tai lieu tai day"""
    return x**2

print(square.__doc__)


# Bài 9:
# 
# Câu hỏi: 
# 
# Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance
# 
# Gợi ý:
# 
# Khi định nghĩa tham số instance, cần thêm nó vào __init__
# Bạn có thể khởi tạo một đối tượng với tham số bắt đầu hoặc thiết lập giá trị sau đó.

# In[ ]:


class Persion:
    'Khoi tao class persion'
    
    persion_name1 = 'Luc'
    def __init__(self, persion_name = None):
        self.persion_name1 = persion_name
        
    def getPersion(self):
        return self.persion_name1
        
persion1 = Persion('Nam')
print(persion1.getPersion())

print('id :',id(persion1.persion_name1))
persion1.persion_name1 = 'Luc'
print(persion1.getPersion())


# Bài 10: 
# 
# Câu hỏi:
# 
# Viết chương trình và in giá trị theo công thức cho trước: `Q = √([(2 * C * D)/H])` (bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H]. 
# 
# Với giá trị cố định của C là 50, H là 30. 
# D là dãy giá trị tùy biến, được nhập vào từ giao diện người dùng, các giá trị của D được phân cách bằng dấu phẩy.
# 
# Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.

# In[ ]:


def calculator_value(D, resuilt):
    if not D:
        return resuilt
    C, H = [50, 30]
    resuilt.append(str(int((math.sqrt((2 * C * int(D.pop()))/H)))))
    calculator_value(D, resuilt)

# Input function
input_d = input('Input array')
input_d = input_d.split(',')

Resuilt = []
calculator_value(input_d, Resuilt)

swap_resuilt = []
while Resuilt:
    swap_resuilt.append(Resuilt.pop())
    
print(','.join(swap_resuilt))


# ## Bài 11:
# 
# Câu hỏi:
# 
# Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều. Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.
# 
# Lưu ý: i=0,1,…,X-1; j=0,1,…,Y-1. 
# 
# Ví dụ: Giá trị X, Y nhập vafp là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
# 
# Gợi ý:
# 
# Viết lệnh để nhận giá trị X, Y từ giao diện điều khiển do người dùng nhập vào.

# In[ ]:


X, Y = [int(x) for x in input('Enter Values: ').split(',')]

arr_xy = []
for i in range(X):
    arr_j = []
    for j in range(Y):
        arr_j.append(i*j)
    arr_xy.append(arr_j)
    
print(arr_xy)


# In[ ]:


a = [[2,3], [3,4]]
a[0][1]


# ## Bài 11:
# 
# Câu hỏi:
# 
# Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, phân tách nhau bởi dấu phẩy và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.
# 
# Giả sử đầu vào được nhập là: without,hello,bag,world, thì đầu ra sẽ là: bag,hello,without,world.
# 
# Gợi ý:
# 
# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.

# In[ ]:


input_string = str(input('Enter values')).split(',')
print(','.join(sorted(input_string)))


# Bài 12:
# 
# Câu hỏi:
# 
# Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào, chuyển các dòng này thành chữ in hoa và in ra màn hình. Giả sử đầu vào là:
# 
# Hello world
# Practice makes perfect
# 
# Thì đầu ra sẽ là:
# 
# HELLO WORLD
# PRACTICE MAKES PERFECT
# 
# Gợi ý:
# 
# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.

# In[ ]:


resuilt = []
while True:
    s = input()
    if s:
        resuilt.append(str.upper(s))
    else:
        break
    
print(resuilt)


# Bài 13:
# 
# Câu hỏi:
# 
# Viết một chương trình chấp nhận đầu vào là một chuỗi các từ tách biệt bởi khoảng trắng, loại bỏ các từ trùng lặp, sắp xếp theo thứ tự bảng chữ cái, rồi in chúng.
# 
# Giả sử đầu vào là: hello world and practice makes perfect and hello world again
# 
# Thì đầu ra là: again and hello makes perfect practice world
# 
# Gợi ý:
# 
# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
# 
# Sử dụng set để loại bỏ dữ liệu trùng lặp tự động và dùng sorted() để sắp xếp dữ liệu.

# In[ ]:


str_input = input().split(' ')

# Cach ngu
check = str_input
temp = []
while check:
    check_temp = check.pop()
    flg = False
    for x in check:
        if x == check_temp:
            flg = True
    if not flg:
        temp.append(check_temp)
print(sorted(temp))

# Cach khon

str_input = input().split(' ')
print(sorted(set(str_input)))


# Bài 14:
# 
# Câu hỏi:
# 
# Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không. Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.
# 
# Ví dụ đầu vào là: 0100,0011,1010,1001
# 
# Đầu ra sẽ là: 1010

# In[ ]:


# Cách ngu
def convertBit(bit_value):
    arr_bit = [int(x) for x in list(bit_value)]
    value = 0
    i = 0
    while arr_bit:
        value += arr_bit.pop() * (2**i)
        i += 1
    return value

values_in = [x for x in (input()).split(',')]

values_div_5 = []
for x in values_in:
    if convertBit(x) % 5 == 0:
        values_div_5.append(x)
        
print(','.join(values_div_5))
# Cách bớt ngu
values_in = [x for x in (input()).split(',')]
values_div_5 = []
for val in values_in:
    if int(val, 2) % 5 == 0 :
        values_div_5.append(val)
    
print(','.join(values_div_5))


# In[ ]:


for i in range(0, 8):
    print(i)


# In[ ]:


int('1010', 2)


# Bài 15:
# 
# Câu hỏi:
# 
# Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này) sao cho tất cả các chữ số trong số đó là số chẵn. In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.
# 
# Gợi ý:
# 
# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.

# In[ ]:


val_div_2 = []
resuilt = []

def check_div_2(val):
    val = list(str(val))
    return all(x % 2 == 0 for x in val)

for x in range(1000, 3001, 2):
    if check_div_2(x):
        resuilt.append(str(x))

print(','.join(resuilt))


# Bài 16:
# 
# Câu hỏi:
# 
# Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó. Giả sử đầu vào sau được cấp cho chương trình: hello world! 123
# 
# Thì đầu ra sẽ là: 
# 
# Số chữ cái là: 10
# Số chữ số là: 3
# 
# Gợi ý:
# 
# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.

# In[ ]:


input_val = list(str(input()).trim())
count = {'num' : 0, 'char' : 0}

for x in input_val:
    if x.isnumeric():
        count['num'] += 1
    elif x.isalpha():
        count['char'] += 1
        
print(count)


# Bài 17:
# 
# Câu hỏi:
# 
# Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.
# 
# Giả sử đầu vào là: Quản Trị Mạng
# 
# Thì đầu ra là:
# 
# Chữ hoa: 3
# 
# Chữ thường: 8
# 
# Gợi ý:
# 
# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.

# In[ ]:


count = {'upper': 0, 'lower': 0}

val_input = list(str(input()))

for val in val_input:
    if val.islower():
        count['lower'] += 1
    elif val.isupper():
        count['upper'] += 1
    else:
        pass
print(count)


# ## Bài 18:
# 
# Câu hỏi:
# 
# Viết một chương trình tính giá trị của a+aa+aaa+aaaa với a là số được nhập vào bởi người dùng.
# 
# Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234
# 
# Gợi ý:
# 
# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.

# In[ ]:


a_in = int(input())

# Cach ngu
resuilt = ''

resuilt = str(a_in) + str(a_in * 2) + str(a_in * 3) + str(a_in * 4)
print(resuilt)

# Cach it ngu
resuilt = ''
for i in range(4):
    resuilt += str(a_in * (i+1))
print(resuilt)



# In[ ]:


# Cach do ngu nhat
a_in = int(input())
a_in = int('%s%s%s%s' %(a_in, a_in * 2, a_in * 3, a_in * 4))
print(a_in)


# In[ ]:


# Cach do ngu nhat
a_in = int(input())
cal = 1
sum_cal = 0 
for x in range(1, 4):
    sum_cal = sum_cal +  a_in
1 = 0 + 1
11 = 10 + 1
111 = 100 + 10 + 1
111 = 1000 + 100 + 10 + 1


# # Bài 19:
# 
# Câu hỏi:
# 
# Sử dụng một danh sách để lọc các số lẻ từ danh sách được người dùng nhập vào.
# 
# Giả sử đầu vào là: 1,2,3,4,5,6,7,8,9 thì đầu ra phải là: 1,3,5,7,9
# 
# Gợi ý:
# 
# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.

# In[ ]:


val_in = str(input()).split(',')

# Cách ngu
resuilt = []
for x in val_in:
    if (int(x) % 2 == 1):
        resuilt.append(x)
        
print(','.join(resuilt))

# Cách khôn
resuilt = [x for x in val_in if int(x) % 2 == 1]
print(','.join(resuilt))


# In[ ]:


val_in = set([int(x) for x in str(input()).split(',')])
le = set(range(1, max(val_in)+1, 2))
result = le & val_in
print(result)


# ## Bài 20:
# 
# Câu hỏi:
# 
# Viết chương trình tính số tiền thực của một tài khoản ngân hàng dựa trên nhật ký giao dịch được nhập vào từ giao diện điều khiển. 
# 
# Định dạng nhật ký được hiển thị như sau:
# 
# D 100
# W 200
# 
# (D là tiền gửi, W là tiền rút ra).
# 
# Giả sử đầu vào được cung cấp là:
# 
# D 300
# 
# D 300
# 
# W 200
# 
# D 100
# 
# Thì đầu ra sẽ là:
# 
# 500
# 
# Gợi ý:
# 
# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.

# In[8]:


account = 0
def check_format(trans):
    check = re.match(r'^[D,Z] [1-9]|[1-9][0-9]|[1-9][0-9[0-9]$', trans)
    if check:
        return True
    return False

while True:
    money = input()
    if not money:
        break
        
    if not check_format(money):
        print ('Format Error')
        break    
    money = money.split(' ')
    
    
    if (money[0] == 'D'):
        account += int(money[1])
    else:
        account = account - int(money[1])
    print(account)
    


# ## Bài 21:
# 
# Câu hỏi:
# 
# Một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký. Viết chương trình để kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào.
# 
# Các tiêu chí kiểm tra mật khẩu bao gồm:
# 
# 1. Ít nhất 1 chữ cái nằm trong [a-z]
# 2. Ít nhất 1 số nằm trong [0-9]
# 3. Ít nhất 1 kí tự nằm trong [A-Z]
# 4. Ít nhất 1 ký tự nằm trong [$ # @]
# 5. Độ dài mật khẩu tối thiểu: 6
# 6. Độ dài mật khẩu tối đa: 12
# 
# Chương trình phải chấp nhận một chuỗi mật khẩu phân tách nhau bởi dấu phẩy và kiểm tra xem chúng có đáp ứng những tiêu chí trên hay không. Mật khẩu hợp lệ sẽ được in, mỗi mật khẩu cách nhau bởi dấu phẩy.
# 
# Ví dụ mật khẩu nhập vào chương trình là: ABd1234@1,a F1#,2w3E*,2We3345
# 
# Thì đầu ra sẽ là: ABd1234@1

# In[17]:


def check_format_pass(pass_in):
    if (len(pass_in) < 6) or (len(pass_in)>12):
        return False
    check_arr = [r'[a-z]', r'[0-9]', r'[A-Z]', r'[$]|[#]|[@]']
    return all(re.findall(x, pass_in) for x in check_arr)

print(check_format_pass(input()))


# ## Bài 22:
# 
# Câu hỏi:
# 
# Viết chương trình sắp xếp tuple (name, age, score) theo thứ tự tăng dần, name là string, age và height là number. Tuple được nhập vào bởi người dùng. Tiêu chí sắp xếp là:
# 
# Sắp xếp theo name sau đó sắp xếp theo age, sau đó sắp xếp theo score. Ưu tiên là tên > tuổi > điểm.
# 
# Nếu đầu vào là:
# 
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# 
# Thì đầu ra sẽ là:
# 
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
# 
# Gợi ý:
# 
# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
# 
# Sử dụng itemgetter để chấp nhận nhiều key sắp xếp.

# In[52]:


in_value = [tuple(x.split(',')) for x in input().split(' ')]

sorted(in_value, key= itemgetter(0, 1, 2))


# Bài 23:
# 
# Câu hỏi:
# 
# Xác định một class với generator có thể lặp lại các số nằm trong khoảng 0 và n, và chia hết cho 7.
# 
# Gợi ý:
# 
# Sử dụng yield.

# In[73]:


def generator(n):
    for i in range(0, n, 7):
        yield i
        
gen = generator(100)

for g in gen:
    print(g)


# # Bài 24:
# 
# Câu hỏi:
# 
# Một Robot di chuyển trong mặt phẳng bắt đầu từ điểm đầu tiên (0,0). Robot có thể di chuyển theo hướng UP, DOWN, LEFT và RIGHT với những bước nhất định. Dấu di chuyển của robot được đánh hiển thị như sau:
# 
# UP 5
# 
# DOWN 3
# 
# LEFT 3
# 
# RIGHT 3
# 
# Các con số sau phía sau hướng di chuyển chính là số bước đi. Hãy viết chương trình để tính toán khoảng cách từ vị trí hiện tại đến vị trí đầu tiên, sau khi robot đã di chuyển một quãng đường. Nếu khoảng cách là một số thập phân chỉ cần in só nguyên gần nhất.
# 
# Ví dụ: Nếu tuple sau đây là input của chương trình:
# 
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# 
# thì đầu ra sẽ là 2.
# 
# Gợi ý:
# 
# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.

# In[112]:


seark_Key = r'UP \d|DOWN \d|LEFT \d|RIGHT \d'
move_input = 'UP 5 DOWN 3 LEFT 3 RIGHT 2'
in_val = [x.split(' ') for x in re.findall(seark_Key, move_input)]

# Cach lang nhang, phuc tap
X0 = [0, 0]
X1 = [0, 0]

def distance(X1, X2):
    return math.sqrt((X1[0] - X1[1])**2 - (X2[0] - X2[1])**2)

move = {'UP': [0, 1], 'DOWN': [0, -1], 'RIGHT': [1, 0], 'LEFT': [-1, 0]}

for move_key, move_value in in_val:
    X0[0] = X0[0] + move[move_key][0] * int(move_value)
    X0[1] = X0[1] + move[move_key][1] * int(move_value)
    
print(X0, X1)
print('Distance is : ', round(distance(X0, X1)))


# In[116]:


seark_Key = r'UP \d|DOWN \d|LEFT \d|RIGHT \d'
move_input = 'UP 5 DOWN 3 LEFT 3 RIGHT 2'
in_val = [x.split(' ') for x in re.findall(seark_Key, move_input)]

start_xy = [0, 0]

for move in (in_val):
    move_key = move[0]
    move_value = move[1]
    
    if move_key == 'UP' :
        start_xy[1] += int(move_value)
    if move_key == 'DOWN':
        start_xy[1] -= int(move_value)
    if move_key == 'LEFT':
        start_xy[0] -= int(move_value)
    if move_key == 'RIGHT':
        start_xy[0] += int(move_value)
        
start_xy


# ### Bài 25:
# 
# Câu hỏi:
# 
# Viết chương trình tính tần suất các từ từ input. Output được xuất ra sau khi đã sắp xếp theo bảng chữ cái.
# 
# Giả sử input là: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# 
# Thì output phải là:
# 
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
# 
# Gợi ý:
# 
# Trong trường hợp dữ liệu đầu vào được cung cấp cho câu hỏi, nó phải được giả định là một input được nhập từ giao diện điều khiển.

# In[169]:


# Cachs vai ngu

in_value = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3'.split(' ')

index = set(in_value)
result = zip([1]*len(index), index)


def count_char(str, str_arr):
    count = 0
    for s in str_arr:
        if s == str:
            count += 1
    return count

result = {key : values for values, key in result}

for ind in index:
    s = count_char(ind, in_value)
    result[ind] = s
    
print(result)


# In[177]:


# Cách khôn

in_value = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3'.split(' ')

numbers = dict()

for x in in_value:
    if x in numbers:
        numbers[x] += 1
    else:
        numbers[x] = 1
    
print(numbers)

# https://www.lifewithpython.com/2015/05/python-dict-default-value.html


# In[188]:


# Cách khôn hơn

in_value = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3'.split(' ')

numbers = dict()

# get(x, 0) Nếu giá trị ở x đã tồn tại, trả về giá trị, x, nếu không trả về default = 0
for x in in_value:
    numbers[x] = numbers.get(x, 0) + 1
    
numbers

