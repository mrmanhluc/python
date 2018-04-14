
# coding: utf-8

# In[32]:


import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


def remove_border(axes=None, top=False, right=False, left=True, bottom=True):
    """
    Minimize chartjunk by stripping out unnecesasry plot borders and axis ticks
    
    The top/right/left/bottom keywords toggle whether the corresponding plot border is drawn
    """
    ax = axes or plt.gca()
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)
    
    #turn off all ticks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')
    
    #now re-enable visibles
    if top:
        ax.xaxis.tick_top()
    if bottom:
        ax.xaxis.tick_bottom()
    if left:
        ax.yaxis.tick_left()
    if right:
        ax.yaxis.tick_right()


# In[3]:


URL = r'D:\02_Python\temp\00_data\imdb_top_10000.txt'
dt_move_info = pd.read_csv(URL, delimiter = '\t', header = None)


# ## 1. Read data
# After loaded data, changing the columns name

# In[4]:


old_columns_name = dt_move_info.columns
new_columns_name = ['ID', 'move_name', 'year', 'idbm', 'numbers_review', 'run_time', 'genres']
rename = {x:y for x, y in zip(old_columns_name, new_columns_name)}
dt_move_info.rename(columns = rename, inplace = True)
dt_move_info.head()


# ## 2. Clean the DataFrame
# 
# There are several problems with the DataFrame at this point:
# 
# The runtime column describes a number, but is stored as a string
# The genres column is not atomic -- it aggregates several genres together. This makes it hard, for example, to extract which movies are Comedies.
# The movie year is repeated in the title and year column
# Fixing the runtime column
# The following snipptet converts a string like '142 mins.' to the number 142:
# 
# Chuyển định dạng columns length qua Int, xóa mins

# In[ ]:


read_file = pd.read_csv


# In[5]:


# Kiểm tra data type của các columns
# Cách 1
print(dt_move_info.info())

dt_move_info['run_time_clean'] = dt_move_info.run_time.apply(lambda x: int(re.findall(r'\d+', x)[0]))
print(dt_move_info.info())


# In[86]:





# In[97]:


a = [123]
type(a[0])


# In[6]:


# Cach 2

dt_move_info['run_time_clean'] = [float(x.split(' ')[0]) for x in dt_move_info.run_time]
dt_move_info[:5]


# ## 3.Splitting up the genres
# 
# We can use the concept of indicator variables to split the genres column into many columns. Each new column will correspond to a single genre, and each cell will be True or False.

# ### Stupied ways

# In[7]:


genres_split = [set(str(x).split('|')) for x in dt_move_info.genres]
genres_index_uniquee = [set(str(x).split('|')) for x in dt_move_info.genres.unique()]

# Union. 
union_genres = set()
for x in genres_index_uniquee:
        union_genres = union_genres | x

tbl_genre = dict()
for col in union_genres:
    temp = [set([col]).issubset(x) for x in genres_split]
    tbl_genre.update({col: temp})
    
tbl_genre = pd.DataFrame(tbl_genre)
tbl_genre[:4]


# In[8]:


count_genres = dict()

for genres in tbl_genre:
    sum_genres = int(tbl_genre[genres].sum())
    count_genres.update({genres: [sum_genres]})
    
count_genres = pd.DataFrame(count_genres)
count_genres.plot.bar()


# In[133]:





# In[193]:


tbl_genre = dict()
for col in union_genres:
    print(type(col))
    break

pd.DataFrame(tbl_genre)


# In[197]:


temp = {'a':[True, False, True]}
pd.DataFrame(temp)


# ### Smarth Ways

# In[9]:


set_genres = set()
for m in dt_move_info.genres:
    set_genres.update(x for x in str(m).split('|'))

dt_move_info_cp = dt_move_info

for genre in set_genres:
    dt_move_info_cp[genre] = [set([genre]).issubset(str(x).split('|')) for x in dt_move_info_cp.genres]

# Đếm tổng số lượng thể loại các bộ phim
dt_move_info_cp[list(set_genres)].sum(). plot.bar()


# In[282]:


dt_move_info.genres.apply(lambda x: str(x).split('|'))


# ## 4.Removing year from the title
# We can fix each element by stripping off the last 7 characters
# 
# The Shawshank Redemption (1994)	 -> The Shawshank Redemption

# In[10]:


dt_move_info_cp = dt_move_info

def delete_year(move_name):
    if re.match(r'.*\(\d\d\d\d\)$', move_name) :
        return move_name[: -6]
    return move_name

dt_move_info_cp.move_name = [delete_year(name)  for name in dt_move_info_cp.move_name]

dt_move_info_cp


# In[290]:


a = [1,2,3,4]
a[-2 :]


# In[337]:


a = 'as;lkdlaasdasskldlas2)'
if re.match(r'.*\(\d\d\d\d\)$', a):
    print(a[:-6])
else:
    print(a)


# ## 5 Describle Data

# In[414]:


dt_move_info_cp.describe


# In[11]:


dt_move_info_cp[['year', 'idbm', 'numbers_review', 'run_time_clean']].describe()


# In[398]:


a = set('Adventure')
aa = 'Action|Adventure|Fantasy|Sci-Fi'.split('|')
a.issubset(aa)


#     5.1 Check nan

# In[12]:


dt_move_info_cp.isna().sum()[:10]


# ### 6. Draw chart
# 
# ### 1. Vẽ chart thể hiện số lượng bộ phim qua các năm (Từ 1980)

# In[450]:


dt_move_info_cp.groupby('year').count().ID.plot.bar()


# In[13]:


pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 100)
dt_move_info_cp[dt_move_info_cp.year > 1980].groupby('year').count().ID.plot(kind = 'bar', color='black', subplots = True, figsize = (20, 10))


# In[458]:


pd.Data


# ### kind : Định dạng chart
# * line : line plot (default)
# * bar : vertical bar plot
# * barh : horizontal bar plot
# * hist : histogram
# * box : boxplot
# * kde : Kernel Density Estimation plot
# * density : same as kde
# * area : area plot
# * pie : pie plot
# * scatter : scatter plot
# * hexbin : hexbin plot
# 
# ### figsize = (20, 10) : Kích thước chart, theo inch
# 
# ### Color = ('black') : Màu chart

# ### 2. Vẽ chart thể hiện điểm IDBM
# 
# Bins = 20. Giá trị được chia 20 khoảng, các giá trị tương đương sẽ được chia vào các nhóm tương đương

# In[14]:


dt_move_info_cp.idbm

idbm_round = [round(x) for x in dt_move_info_cp.idbm]
plt.plot()


# In[15]:


dt_move_info_cp.idbm.plot.hist(figsize = (20, 10), bins = 20, color = '#cccccc', title = 'IDBM Score')
remove_border()


# ### 3 .Vẽ chart thể hiện runtime

# In[16]:


dt_move_info_cp.run_time_clean.plot.hist(color = '#cccccc', bins = 50, figsize = (20,10))
remove_border()


# ### 4. Biểu đồ scarter thể hiện điểm IMDB qua các năm

# In[17]:


plt_idbm = plt.scatter(dt_move_info_cp.year, dt_move_info_cp.idbm, lw = 0, alpha=.04, color='b')
remove_border()
#plt.scatter(data.year, data.score, lw=0, alpha=.08, color='k')


# ### * * 5. Scater thể hiện số lượng Votes, cùng IMBD

# In[18]:


plt.scatter(dt_move_info_cp.numbers_review, dt_move_info_cp.idbm, lw = 0, alpha=.08, color='b')
remove_border()
plt.xscale('log')


# # 7. Thao tác trên Data
# 
# ### 7.1 Tìm giá trị vote, có số lượng 9^4 và IMDB > 7

# In[19]:


dt_move_info_cp[(dt_move_info.numbers_review > 10e4) & (dt_move_info.idbm > 8)][['move_name', 'year', 'idbm', 'numbers_review']][:20]


# ### 7.2 In ra danh sách những bộ phim có idbm thấp nhât

# In[20]:


dt_move_info_cp[dt_move_info_cp.idbm == dt_move_info_cp.idbm.min()]


# ### 7.3 Danh sách bộ phim có IDBM cao nhất

# In[21]:


dt_move_info_cp[dt_move_info_cp.idbm == dt_move_info_cp.idbm.max()]


# ### 7.4 Danh sách phim IDBM > 8 nhưng không thuộc năm [ 1994 : 2000]

# In[22]:


dt_move_info_cp[(dt_move_info_cp.idbm > 8) & (dt_move_info_cp.year > 2000) & (dt_move_info_cp.year < 1994)]


# ### 7.5 Tính tổng số lượng trong nhóm các thể loại phim, sắp xếp theo thứ tự giảm dần

# In[87]:


# Step 1 : Lấy danh sách các thể loại phim, sử dụng set update
dt_move_info_cp.genres
genres_set = set()
for x in dt_move_info_cp.genres:
    genres_set.update(str(x).split('|'))

# Step 2 ; Tính tổng các thể loại phim
values = dt_move_info_cp[list(genres_set)].sum()

# Step 3 : Sắp xếp theo thứ tự tăng dần
values.sort_values(ascending = False, inplace=True)

pd.DataFrame(values).plot.bar(figsize = (20, 5), color = '#dddddd')

remove_border()


# ## 8. Phân tích nâng cao

# ### 8.1 Vẽ biểu đồ Scarter (Year, IMDB), vẽ Line chart cho Means(IMDB)

# In[148]:


# Step 1. Tính Means imdb
mean_idbm = dt_move_info_cp[['year', 'idbm']].groupby('year').mean()

# Step 2. Sort theo index, tức sort theo năm theo thứ tự năm tăng dần
mean_idbm.sort_index()

# Step 3. Vẽ line chart cho mean_idbm theo year
plt.plot(mean_idbm, 'ro-')

# Step 4. Vẽ scater chart cho imdb theo year
plt.scatter(dt_move_info_cp.year,
            dt_move_info_cp.idbm,
            lw = 0, 
            alpha=.08, 
            color='b'
           )

remove_border()


# In[122]:


get_ipython().run_line_magic('pinfo', 'mean_idbm.plot.line')

