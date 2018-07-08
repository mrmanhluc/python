
# coding: utf-8

# In[1]:





# In[13]:


count_plush = []

for i in range(10):
    if(data>data[-1]):
        print(data[i])


# In[19]:


range(1, 10)[0]


# In[78]:


count_up_arr = []
count_down_arr = []

count_down, count_up = 0, 0

for i in range(1, data):
    if(data[i] > data[i-1]):
        count_up += 1
        count_down_arr.append(count_down)
        count_down = 1
        print(count_up, count_down, data[i])
    if(data[i] < data[i-1]):
        count_up_arr.append(count_up)
        count_down += 1
        count_up = 1
    if(data[i] == data[i-1]):
        count_down += 1
        count_up += 1
        
print(max(count_up_arr))
print(max(count_down_arr))


# In[29]:





# In[35]:


leng = int(input())
data = [int(x) for x in input().split()]
count_down, count_up = 0,0
arr_down, arr_up = [1],[1]
for i in range(0, len(data) - 1):
    count_down = count_down * int(data[i] >= data[i+1]) + int(data[i] >= data[i+1])
    arr_down.append(count_down+1)
    count_up = count_up * int(data[i] <= data[i+1]) + int(data[i] <= data[i+1])
    arr_up.append(count_up+1)

    
print(max(arr_up), max(arr_down))

