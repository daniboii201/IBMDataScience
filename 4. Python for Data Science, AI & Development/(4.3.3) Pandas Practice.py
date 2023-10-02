### Exercise 1 Pandas: DataFrame and Series

# let us import the Pandas Library
import pandas as pd

#Define a dictionary 'x'
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}
#casting the dictionary to a DataFrame
df = pd.DataFrame(x)
#display the result df
df
#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
x
#check the type of x
type(x)
#Retrieving the Department, Salary and ID columns and assigning it to a variable z
z = df[['Department','Salary','ID']]
z

#### Exercise 1: Create a dataframe to display the result as below:
x2 = {'Student': ['David','Samuel', 'Terry', 'Evan'], 'Age': [27, 24, 22, 32], 'Country': ['UK', 'Canada', 'China', 'US'], 
      'Course':['Python','Data Structures','Machine Learning','Web Development'], 'Marks':[85,72,89,76]}
df1=pd.DataFrame(x2)
df1
b=df1[['Marks']]
b
c=df1[['Country','Course']]
c
# Get the Student column as a series Object
x = df1['Student']
x
#check the type of x
type(x)

#### Exercise 2: loc() and iloc()

# loc() is a label-based data selecting method which means that we have to pass the name of the row or column that we want to select. 
    # This method includes the last element of the range passed in it.

### Simple syntax for your understanding:
### loc[row_label, column_label]

# iloc() is an indexed-based selecting method which means that we have to pass an integer index in the method to select a specific row/column. 
    # This method does not include the last element of the range passed in it.

### Simple syntax for your understanding:
### iloc[row_index, column_index]

# Access the value on the first row and the first column
df.iloc[0, 0]
# Access the value on the first row and the third column
df.iloc[0,2]
# Access the column using the name
df.loc[0, 'Salary']

# Let us create a new dataframe called 'df2' and assign 'df' to it. Now, let us set the "Name" column as an index column using the method set_index().
df2=df
df2=df2.set_index("Name")
#To display the first 5 rows of new dataframe
df2.head()
#Now, let us access the column using the name
df2.loc['Jane', 'Salary']

# Use the loc() function,to get the Department of Jane in the newly created dataframe df2.
df2.loc['Jane','Department']
# Use the iloc() function to get the Salary of Mary in the newly created dataframe df2.
df2.iloc[3,2]

#### Exercise 3: Slicing

# let us do the slicing using old dataframe df
df.iloc[0:2, 0:3]
#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
df.loc[0:2,'ID':'Department']
#let us do the slicing using loc() function on new dataframe df2 where index column is Name having labels: Rose, John and Jane
df2.loc['Rose':'Jane', 'ID':'Department']

# using loc() function, do slicing on old dataframe df to retrieve the Name, ID and department of index column having labels as 2,3
df.loc[2:3,'Name':'Department']