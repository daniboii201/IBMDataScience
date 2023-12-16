# import pandas library
import pandas as pd
import numpy as np

# Read the online file by the URL provides above, and assign it to variable "df"
other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)

# After reading the data set, we can use the <code>data_frame.head(n)</code> method to check the top n rows of the data frame, 
# where n is an integer. Contrary to <code>data_frame.head(n)</code>, <code>data_frame.tail(n)</code> will show you the 
# bottom n rows of the data frame.
# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)

### Question #1: Check the bottom 10 rows of data frame "df"
df.tail(5)

### Add headers. First, create a list "headers" that include all column names in order. 
# Then, use <code>dataframe.columns = headers</code> to replace the headers with the list you created.
# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)
# Replace headers and recheck our dataframe
df.columns = headers
df.columns
# You can also see the first 10 entries of the updated data frame and note that the headers are updated.
df.head(10)
# Now, we need to replace the "?" symbol with NaN so the dropna() can remove the missing values:
df1=df.replace('?',np.NaN)
# You can drop missing values along the column "price" as follows:
df=df1.dropna(subset=["price"], axis=0)
df.head(20)
## Here, `axis=0` means that the contents along the entire row will be dropped wherever the entity 'price' is found to be NaN
# Now, you have successfully read the raw data set and added the correct headers into the data frame.

### QUESTION 2: Find the name of the columns of the dataframe
print(df.columns)

## Save Dataset
df.to_csv("automobile.csv", index=False)

### Data Types

# Data has a variety of types. The main types stored in Pandas data frames are object, float, int, bool and datetime64. 
# In order to better learn about each attribute, you should always know the data type of each column. In Pandas:
df.dtypes
print(df.dtypes)

### Describe

# If we would like to get a statistical summary of each column such as count, column mean value, column standard deviation, etc., 
# use the describe method:
df.describe()
# describe all the columns in "df" 
df.describe(include = "all")

### QUESTION 3: Apply the  method to ".describe()" to the columns 'length' and 'compression-ratio'.
df[['length', 'compression-ratio']].describe()

### Info: It provides a concise summary of your data frame. 
# This method prints information about a data frame including the index dtype and columns, non-null values and memory usage.
df.info()