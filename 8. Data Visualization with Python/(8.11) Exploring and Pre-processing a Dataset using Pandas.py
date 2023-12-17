import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

### Let's download and import our primary Canadian Immigration dataset using *pandas*'s `read_excel()` method.
df_can = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)
print('Data read into a pandas dataframe!')

### Let's view the top 5 rows of the dataset using the `head()` function.
df_can.head()
### We can also view the bottom 5 rows of the dataset using the `tail()` function.
df_can.tail()
### When analyzing a dataset, it's always a good idea to start by getting basic information about your dataframe. 
### We can do this by using the `info()` method. This method can be used to get a short summary of the dataframe.
df_can.info(verbose=False)
### To get the list of column headers we can call upon the data frame's `columns` instance variable.
df_can.columns
### Similarly, to get the list of indices we use the `.index` instance variables.
df_can.index
### Note: The default type of intance variables `index` and `columns` are **NOT** `list`.
print(type(df_can.columns))
print(type(df_can.index))
### To get the index and columns as lists, we can use the `tolist()` method.
df_can.columns.tolist()
df_can.index.tolist()
print(type(df_can.columns.tolist()))
print(type(df_can.index.tolist()))
### To view the dimensions of the dataframe, we use the `shape` instance variable of it.
df_can.shape # size of dataframe (rows, columns)

### Let's clean the data set to remove a few unnecessary columns. We can use *pandas* `drop()` method as follows:
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True) 
df_can.head(2) # in pandas axis=0 represents rows (default) and axis=1 represents columns.
### Let's rename the columns so that they make sense. We can use `rename()` method by passing in a dictionary of old and 
### new names as follows:
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns
### We will also add a 'Total' column that sums up the total immigrants by country over the entire period 1980 - 2013, as follows:
df_can['Total'] = df_can.sum(axis=1)
df_can['Total']
### We can check to see how many null objects we have in the dataset as follows:
df_can.isnull().sum()
### Finally, let's view a quick summary of each column in our dataframe using the `describe()` method.
df_can.describe()

##### SELECT COLUMN #####

### Example: Let's try filtering on the list of countries ('Country').
df_can.Country  # returns a series
### Let's try filtering on the list of countries ('Country') and the data for years: 1980 - 1985.
df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]] # returns a dataframe
# notice that 'Country' is string, and the years are integers. 
# for the sake of consistency, we will convert all column names to string later on.

##### SELECT ROW #####

df_can.set_index('Country', inplace=True)
df_can.head(3)
# optional: to remove the name of the index
df_can.index.name = None
### Example: Let's view the number of immigrants from Japan (row 87) for the following scenarios:
    #1. The full row data (all columns)
    #2. For year 2013
    #3. For years 1980 to 1985
df_can.loc['Japan'] # 1. the full row data (all columns)
df_can.iloc[87] # alternate methods
df_can[df_can.index == 'Japan']
df_can.loc['Japan', 2013] # 2. for year 2013
df_can.iloc[87, 36] # alternate method, year 2013 is the last column, with a positional index of 36
df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]] # 3. for years 1980 to 1985
df_can.iloc[87, [3, 4, 5, 6, 7, 8]] # Alternative Method

##### Exercise: Let's view the number of immigrants from **Haiti** for the following scenarios: 

# 1. the full row data (all columns)
df_can.loc['Haiti']
#or
df_can[df_can.index == 'Haiti']
# 2. for year 2000
df_can.loc['Haiti', 2000]       
#  3. for years 1990 to 1995
df_can.loc['Haiti', [1990, 1991, 1992, 1993, 1994, 1995]]

##### Exercise: Create a list named 'year' using map function for years ranging from 1990 to 2013.
# Then extract the data series from the dataframe df_can for Haiti using year list. 
year = list(map(str, range(1990, 2014)))
haiti = df_can.loc['Haiti', year] # passing in years 1990 - 2013

##### Filtering based on a criteria
# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)
# 2. pass this condition into the dataFrame
df_can[condition]
# we can pass multiple criteria in the same line.
# let's filter for AreaNAme = Asia and RegName = Southern Asia
df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]

##### Exercise: Fetch the data where AreaName is 'Africa' and RegName is 'Southern Africa'.
# Display the dataframe and find out how many instances are there?
df_can[(df_can['Continent']=='Africa') & (df_can['Region']=='Southern Africa')]

df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
top_5 = df_can.head(5)
top_5

##### Exercise: Find out top 3 countries that contributes the most to immigration to Canda in the year 2010.
# Display the country names with the immigrant count in this year

df_can.sort_values(by='2010', ascending=False, axis=0, inplace=True)
top3_2010 = df_can['2010'].head(3)
top3_2010