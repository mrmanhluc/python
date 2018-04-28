
# coding: utf-8

# In[157]:


import pandas as pd
import codecs as cd
import glob
import xlsxwriter
import os
from dateutil import parser
import re


# ## Common Function
# 
# #### 1. Get_Columns_Metrics
# 
# Input Data = DataFrame
# 
# Output : 
# 
# | Columns_name       | Tên columns            |
# |--------------------|------------------------|
# | Values_Range       | Giá trị Min : Max      |
# | Null_nums          | Số lượng giá trị Nulls |
# | Rows_nums          | Tổng số rows           |
# | Unique_values      | Giá trị unique         |
# | Unique_nums        | Tổng số lượng unique   |
# | Category_types     | Loại Category type     |
# | Unique_values_rate | Tỉ lệ unique           |
#     

# In[158]:


def to_number(str):
    '''
        Input : String
        Output : Float. If Null values will be return None
    '''
    temp = None
    try:
        temp = float(str)
    except ValueError:
        return None
    return temp

def to_date(column):
    '''
        Input : Pandas Serial
    '''
    tmp_date = []
    for x in column:
        try:
            tmp_date.append(parse(str(x)))
        except ValueError:
            tmp_date.append(None)
    return tmp_date


# In[178]:


def is_date(in_data):
    # Kiểm tra str có phải dạng datetime không
    pattern1 = r'^\d\d\d\d/\d\d/\d\d$'
    pattern2 = r'^\d\d\/\d\d/\d\d$'
    pattern3 = r'^\d\d\d\d\/\d\d\/\d\d \d\d\:\d\d$'
    pattern4 = r'^\d\d\/\d\d\/\d\d \d\d\:\d\d$'
    pattern = [pattern1, pattern2, pattern3, pattern4]

    for pt in pattern:
        if re.match(pt, in_data) is not None:
            return True
    return False

def is_num(in_data):
    return in_data.replace('.','',1).isdigit()


# In[197]:


def get_columns_metrics(In_data):
    '''
    Return list of all file with extendsion is csv in folder
    
    WARNING : - Chua check datatype. Dinh dang Datime. Gia tri max min cua datetime
    1. Datetime => Dua ra khoang tu nam nao toi nam nao => Dua ra thong ke du lieu moi nam chiem bao nhieu %
    2. String => Dua ra duoc do dai cua string => Dua ra khoang max min ki tu
    3. Int => Dua ra gia tri Max Min
    
    :param fileType: DataFrame
    :return: DataFrame and add 3 columns with Category, Size and Sample Data
    '''
    # Validate input
    if isinstance(In_data, pd.DataFrame) == False:
        print('Input values is not Dataframe')
        return
    
    tmp_data = In_data.copy()
    
    rows_nums = len(contentFile)
    
    # IF distinct value numbers > 10% then that values is continues data type
    CATEGORY_DEFINITION = 0.1
    TOP_UNIQUE = 10
    PRECISION = 2
    
    unique_values_values = []
    
    cols_name = []

    # Duyet toan bo columns name cua table 
    for col_name in tmp_data.columns:
       
        # Get each columns name
        cols_name.append(col_name)
        
        # Get unique values
        unique_values = tmp_data[str(col_name)].unique()
        
        # Get numbers of unique values
        unique_nums = len(unique_values)
        
        # Category Type
        category_type = None
        
        # Get rate of each unique values
        unique_values_rate = {}
        
        # Get Null values
        null_nums = tmp_data[col_name].isnull().sum()
        
        # Convert to DataTime if is Datatime
        if is_date(contentFile['最終更新日'].dropna()[:1].values[0]):
            tmp_data[col_name] = pd.to_datetime(tmp_data[col_name], errors= 'coerce').dropna()
            category_type = 'DataTime'
        
        # Get Min, Max values
        min_value, max_value = None, None
        try:
            min_value = float(tmp_data.dropna()[col_name].min())
            max_value = float(tmp_data.dropna()[col_name].max())
        except ValueError:
            min_value, max_value = None, None
        values_range = str([min_value, max_value])
        
        if unique_nums > (rows_nums * CATEGORY_DEFINITION):
            unique_values = None
            unique_nums = None
            category_type = 'Continuous'
        else:
            if unique_nums == 2:
                category_type = 'Binary'
            else:
                category_type = 'Ordinal'
            
            # Dat try catch cho viec /0
            try:
                unique_values_rate = str(pd.Series(contentFile.groupby([col_name])[col_name].count()/rows_nums *100).round(decimals = PRECISION)[:TOP_UNIQUE].to_dict())
            except ValueError:
                unique_values_rate = None
        
        # Add toan bo gia tri vao List theo cau truc [<Gia tri Unique>, <So luong gia tri unique>, <Data Category>]
        add_rows = {
                    'Values_Range' : values_range,
                    'Null_nums' : null_nums,
                    'Rows_nums' : rows_nums,
                    'Unique_values' : str(unique_values), 
                    'Unique_nums' : unique_nums, 
                    'Category_types' : category_type,
                    'Unique_values_rate' : unique_values_rate
                    }
        
        unique_values_values.append(add_rows)

    # Return Table with all values
    return pd.DataFrame(unique_values_values, index = cols_name)


# ## Class Get Info of File

# In[3]:


class File_info(object):
    def get_fileName(url):
        return url[url.rfind('\\') + 1 :]

    def get_Extension(url):
        return url[url.rfind('.') + 1 :]
    
    def get_FileSize(url):
        return os.path.getsize(url)
    


# ## Class Read Content from CSV File

# In[4]:


class ReadFile:
    '''
    Read context of file
    '''
    def __init__(self, in_url):
        self.url = in_url
        
        # Check dieu kien file co phai la csv hay khong
        
        # Get file name from in_url
        self.fileName = File_info.get_fileName(in_url)
        
        # Get file size
        self.file_size = File_info.get_FileSize(in_url)
        
        # Get extendion of file from in url
        self.fileExtention = File_info.get_Extension(in_url)
        
        self.file_context = ''
        self.file_columns = ''
        
        if self.fileExtention == 'csv':
            self.file_context = self.__read_csv()
            self.file_columns = self.file_context.columns
        
    def _read_csv(self):
        with cd.open(self.url, "r", "Shift-JIS", "ignore") as csv_file:
            df = pd.read_table(csv_file, sep=',')
        return df
    
    def getLstColumns(self):
        return self.file_columns
    
    def get_context(self):
        return self.file_context
    
    def get_fileName(self):
        return self.fileName
    
    def get_fileExtension(self):
        return self.fileExtention

    def get_file_Columns(self):
        return self.file_columns
    
    def get_file_size(self):
        return self.file_size


# ## Class Read all file path in folder

# In[5]:


class Read_folder:
    '''
    Read data from csv file
    '''
    def __init__(self, in_folder_url):
        self.folder_url = in_folder_url
        self.csv_url = self.__read_csv_url()
        self.csv_name = self.__read_csv_name()

    def __read_csv_url(self):
        return glob.glob(self.folder_url+'\\*.csv')
    
    def __read_csv_name(self):
        csv_name = []
        for url in self.csv_url:
            csv_name.append(File_info.get_fileName(url))
        return csv_name
    
    def getLst_csv_url(self):
        '''
        Return list of all file with extendsion is csv in folder
        :param fileType: No
        :return: URL with file name
        '''        
        return self.csv_url
    
    def getLst_csv_name(self):
        return self.csv_name


# ## Class write output to Excel file

# In[6]:


class Write_output:
    '''
    Read file in input folder
    '''
    def __init__(self, out_url, sheet_name):
        self.URL = out_url
        self.sheet_name = sheet_name.copy()

    def write_into_sheet(self, data_input, in_sheet_name):
        data_input.to_excel(self.URL, sheet_name=in_sheet_name)

    def create_excel(self, dashboard = False):
        '''
        Create Excel file with sheet name is file in folder
        :return: Excel File
        '''
        tmp_sheet_name = self.sheet_name
        
        if dashboard:
            tmp_sheet_name.append('Dashboard')
            
        workbook = xlsxwriter.Workbook(self.URL)
        for s_name in tmp_sheet_name:
            workbook.add_worksheet(s_name)
        workbook.close()


# # 1. Get infor of file

# In[7]:


# Step 1 : Khởi tạo biến read input
URL = r'D:\01_Project\Lixil Analysis\input\data'
read_input = Read_folder(URL)

# Toàn bộ URL của file csv
print(read_input.getLst_csv_url())

# Toàn bộ file name của file csv trong folder
print(read_input.getLst_csv_name())


# ## 2. Read info of each file in folder

# In[8]:


# Đọc nội dung lần lượt các file trên
finding_data = []
file_name = []
file_columns = []
file_size = []

for file_url in read_input.getLst_csv_url():
    read_file = Read_file(file_url)
    file_name.append(read_file.get_fileName())
    file_columns.append(read_file.get_file_Columns())
    file_size.append(read_file.get_file_size())


# In[9]:


col_num = []
for i in file_columns:
    col_num.append(len(i))

Dashboard = pd.DataFrame({
    'File Name': file_name,
    'Columns numbers': col_num,
    'File Size': file_size
})

write = Write_output('D:\Report.xlsx', file_name)
write.create_excel(True)

## Write Dashboard into Dashboard sheet
write.write_into_sheet(Dashboard, 'dashboard')


#  ## 3. Create Excel which each sheet name is file name

# In[10]:


#Step 1: Lay Url file dau tien
url_file = read_input.getLst_csv_url()[0]

# Step 2 : Doc noi dung file trne
readFile = Read_file(url_file)


# In[34]:


# Step 3 : Get Content
contentFile = readFile.get_context()

# dataFr = pd.concat([dataFr, dataFr1], axis=1)

data_metrics = {}

for url in read_input.getLst_csv_url():
    file = Read_file(url)
    file_context = file.get_context()
    file_context_info = get_columns_metrics(file_context)
    data_metrics[File_info.get_fileName(url)] = file_context_info
    file_context_info.drop(file_context_info.index, inplace=True)
   # break
# In[151]:


get_ipython().run_cell_magic('time', '', 'url = read_input.getLst_csv_url()[1]')


# In[152]:


get_ipython().run_cell_magic('time', '', 'file = Read_file(url)')


# In[153]:


get_ipython().run_cell_magic('time', '', 'file_context = file.get_context()')


# In[154]:


get_ipython().run_cell_magic('time', '', 'file_context_info = get_columns_metrics(file_context)')


# In[172]:


pd.to_datetime(file_context['作成日'], errors= 'coerce').dropna().min()


# ## TEST REGION

# In[186]:


#Step 1: Lay Url file dau tien
url_file = read_input.getLst_csv_url()[1]

# Step 2 : Doc noi dung file trne
readFile = Read_file(url_file)

# Step 3 : Get Content
contentFile = readFile.get_context()


# In[198]:


# is_date(contentFile['ID'].dropna()[:1])

temp = get_Columns_Metrics(contentFile)
temp


# In[145]:


# Nếu taị columns đó là năm tháng
if is_date(temp0['公開開始日'].dropna()[:1][0]):
    


# In[120]:


temp0 = contentFile.copy()

# Function check data type
def get_dataType (str):
    
# Check toan bo column va kieu data

# Duyet toan bo column

for col in temp0.columns:
    print(temp0[col].dropna()[0:1])


# ## Update Region

# In[ ]:


def is_Datetime(str):
    


# In[ ]:


def get_columns_metrics_Update(In_data):
    '''
    Return list of all file with extendsion is csv in folder
    
    WARNING : - Chua check datatype. Dinh dang Datime. Gia tri max min cua datetime
    1. Datetime => Dua ra khoang tu nam nao toi nam nao => Dua ra thong ke du lieu moi nam chiem bao nhieu %
    2. String => Dua ra duoc do dai cua string => Dua ra khoang max min ki tu
    3. Int => Dua ra gia tri Max Min
    
    :param fileType: DataFrame
    :return: DataFrame and add 3 columns with Category, Size and Sample Data
    '''
    # Validate input
    if isinstance(In_data, pd.DataFrame) == False:
        print('Input values is not Dataframe')
        return
    
    tmp_data = In_data.copy()
    
    rows_nums = len(contentFile)
    
    # IF distinct value numbers > 10% then that values is continues data type
    CATEGORY_DEFINITION = 0.1
    TOP_UNIQUE = 10
    PRECISION = 2
    
    unique_values_values = []
    
    cols_name = []

    # Duyet toan bo columns name cua table 
    for col_name in tmp_data.columns:
        # Get each columns name
        cols_name.append(col_name)
        
        # Get unique values
        unique_values = tmp_data[str(col_name)].unique()
        
        # Get numbers of unique values
        unique_nums = len(unique_values)
        
        # Category Type
        category_type = ''
        
        # Get rate of each unique values
        unique_values_rate = {}
        
        # Get Null values
        null_nums = tmp_data[col_name].isnull().sum()
        
        # Get Min, Max values
        min_value, max_value = None, None
        try:
            min_value = float(tmp_data.dropna()[col_name].min())
            max_value = float(tmp_data.dropna()[col_name].max())
        except ValueError:
            min_value, max_value = None, None
        values_range = str([min_value, max_value])
        
        if unique_nums > (rows_nums * CATEGORY_DEFINITION):
            unique_values = None
            unique_nums = None
            category_type = 'Continuous'
        else:
            if unique_nums == 2:
                category_type = 'Binary'
            else:
                category_type = 'Ordinal'
            
            # Dat try catch cho viec /0
            try:
                unique_values_rate = str(pd.Series(contentFile.groupby([col_name])[col_name].count()/rows_nums *100).round(decimals = PRECISION)[:TOP_UNIQUE].to_dict())
            except ValueError:
                unique_values_rate = None
        
        # Add toan bo gia tri vao List theo cau truc [<Gia tri Unique>, <So luong gia tri unique>, <Data Category>]
        add_rows = {
                    'Values_Range' : values_range,
                    'Null_nums' : null_nums,
                    'Rows_nums' : rows_nums,
                    'Unique_values' : str(unique_values), 
                    'Unique_nums' : unique_nums, 
                    'Category_types' : category_type,
                    'Unique_values_rate' : unique_values_rate
                    }
        
        unique_values_values.append(add_rows)

    # Return Table with all values
    return pd.DataFrame(unique_values_values, index = cols_name)

