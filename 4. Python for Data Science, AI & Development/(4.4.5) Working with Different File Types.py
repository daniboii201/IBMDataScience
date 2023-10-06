##### Reading data from CSV in Python
# We use pandas.read_csv() function to read the csv file.
import pandas as pd
url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv'
df = pd.read_csv(url,header=None)
df
# We can add columns to an existing DataFrame using its columns attribute.
df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']
df
# To select the first column 'First Name', you can pass the column name as a string to the indexing operator.
df["First Name"]
# To select multiple columns, you can pass a list of column names to the indexing operator.
df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
df
# loc() : loc() is label based data selecting method which means that we have to pass the name of the row or column which we want to select.
# To select the first row
df.loc[0]
# To select the 0th,1st and 2nd row of "First Name" column only
df.loc[[0,1,2], "First Name" ]
# iloc() : iloc() is a indexed based selecting method which means that we have to pass integer index in the method to select specific row/column.
# To select the 0th, 1st and 2nd row of "First Name" column only
df.iloc[[0,1,2], 0]

### Python’s Transform function returns a self-produced dataframe with transformed values after applying the function specified in its parameter.
import pandas as pd
import numpy as np
# creating a dataframe
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
df
#applying the transform function
df = df.transform(func = lambda x : x + 10)
df
# Now we will use DataFrame.transform() function to find the square root to each element of the dataframe.
result = df.transform(func = ['sqrt'])
result

##### JSON file Format

# Writing JSON to a file
import json
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}
## serialization using dump() function. Syntax: json.dump(dict, file_pointer)
# dictionary – name of the dictionary which should be converted to JSON object. file pointer – pointer of the file opened in write or append mode.
with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)

## serialization using dumps() function. json.dumps() that helps in converting a dictionary to a JSON object.
## dictionary – name of the dictionary which should be converted to JSON object. indent – defines the number of units for indentation
# Serializing json  
json_object = json.dumps(person, indent = 4)  
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object)
print(json_object)


##### Reading JSON to a File
### This process is usually called Deserialization - it is the reverse of serialization. 
### It converts the special format returned by the serialization back into a usable object.

## Using json.load()
# The JSON package has json.load() function that loads the json content from a json file into a dictionary
# It takes one parameter:
# File pointer -- A file pointer that points to a JSON file.

import json 
  # Opening JSON file 
with open('sample.json', 'r') as openfile: 
    json_object = json.load(openfile) # Reading from json file 
print(json_object) 
print(type(json_object))

##### XLSX file format
### XLSX is a Microsoft Excel Open XML file format. It is another type of Spreadsheet file format.
### In XLSX data is organized under the cells and columns in a sheet.

# Reading the data from XLSX file
import pandas as pd
import urllib.request
urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx", "sample.xlsx")
df = pd.read_excel("sample.xlsx")
df

##### XML file format
### Writing with xml.etree.ElementTree
# The xml.etree.ElementTree module comes built-in with Python. It provides functionality for parsing and creating XML documents. 
# ElementTree represents the XML document as a tree. We can move across the document using nodes which are elements and sub-elements of the XML file.

import xml.etree.ElementTree as ET
# create the file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'
# create a new XML file with the results
mydata1 = ET.ElementTree(employee)
# myfile = open("items2.xml", "wb")
# myfile.write(mydata)
with open("new_sample.xml", "wb") as files:
    mydata1.write(files)

### Reading with xml.etree.ElementTree
import pandas as pd 
import xml.etree.ElementTree as etree

# You would need to firstly parse an XML file and create a list of columns for data frame, then extract useful information from the XML file and 
# add to a pandas data frame. Here is a sample code that you can use:
tree = etree.parse("Sample-employee-XML-file.xml")
root = tree.getroot()
columns = ["firstname", "lastname", "title", "division", "building","room"]
datatframe = pd.DataFrame(columns = columns)
for node in root: 
    firstname = node.find("firstname").text
    lastname = node.find("lastname").text 
    title = node.find("title").text  
    division = node.find("division").text     
    building = node.find("building").text   
    room = node.find("room").text   
    datatframe = datatframe.append(pd.Series([firstname, lastname, title, division, building, room], index = columns), ignore_index = True)
datatframe

### Reading xml file using pandas.read_xml function

# Here in xpath we mention the set of xml nodes to be considered for migrating  to the dataframe which in this case is details node under employees.
df=pd.read_xml("Sample-employee-XML-file.xml", xpath="/employees/details") 

### Save data

# Correspondingly, Pandas enables us to save the dataset to csv by using the dataframe.to_csv() method, you can add the file path and name along with quotation marks 
# in the parentheses. For example, if you would save the dataframe df as employee.csv to your local machine, you may use the syntax below:
datatframe.to_csv("employee.csv", index=False)
# csv: pd.read_csv(), df.to_csv()
# json: pd.read_json(), df.to_json()
# excel: pd.read_excel(), df.to_excel()
# hdf: pd.read_hdf(), df.to_hdf()
# sql: pd.read_sql(), df.to_sql()

##### Binary File Format

### Reading the Image file. Python supports very powerful tools when it comes to image processing. Let’s see how to process the images using the PIL library.
# PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities.

# importing PIL 
from PIL import Image 
import urllib.request
# Downloading dataset
urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "dog.jpg")
# Read image 
img = Image.open('dog.jpg') 
# Output Images 
img.show(img)

##### Data Analysis

# We have 768 rows and 9 columns. The first 8 columns represent the features and the last column represent the target/label.
import pandas as pd
path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
df = pd.read_csv(path)

# After reading the dataset, we can use the dataframe.head(n) method to check the top n rows of the dataframe, where n is an integer. 
# Contrary to dataframe.head(n), dataframe.tail(n) will show you the bottom n rows of the dataframe.
# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)
# To view the dimensions of the dataframe, we use the .shape parameter.
df.shape

##### Statistical Overview of dataset

df.info()
# This method prints information about a DataFrame including the index dtype and columns, non-null values and memory usage.
df.describe()

### Identify and handle missing values
## We use Python's built-in functions to identify these missing values. There are two methods to detect missing data:
## .isnull(), .notnull()
## The output is a boolean value indicating whether the value that is passed into the argument is in fact missing data.
missing_data = df.isnull()
missing_data.head(5)
# "True" stands for missing value, while "False" stands for not missing value.

## Count missing values in each column
# "True" represents a missing value, "False" means the value is present in the dataset.
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

## Correct data format
# Check all data is in the correct format (int, float, text or other).
# In Pandas, we use
# .dtype() to check the data type
# .astype() to change the data type
# Numerical variables should have type 'float' or 'int'.
df.dtypes

##### Visualization
### Visualization is one of the best way to get insights from the dataset. Seaborn and Matplotlib are two of Python's most powerful visualization libraries.

# import libraries
import matplotlib.pyplot as plt
import seaborn as sns
labels= 'Diabetic','Not Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()