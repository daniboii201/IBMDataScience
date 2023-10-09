##### Create & Access SQLite database using Python

### Task 1: Create database using SQLite
import sqlite3
conn = sqlite3.connect('INSTRUCTOR.db')

# Cursor class is an instance using which you can invoke methods that execute SQLite statements, fetch data from the 
# result sets of the queries. You can create Cursor object using the cursor() method of the Connection object/class.
cursor_obj = conn.cursor()

### Task 2: Create a table in the database

# In this step we will create a table in the database with following details:
imgsrc="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/images/table.png"

# Before creating a table, let's first if the table already exist or not. To drop the table from a database use **DROP** query. 
# A cursor is an object which helps to execute the query and fetch the records from the database.
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")

# Creating table
table = """ create table IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2));"""
cursor_obj.execute(table)
print("Table is Ready")

### Task 3: Insert data into the table

# We will start by inserting just the first row of data
cursor_obj.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')
# Now use a single query to insert the remaining two rows of data
cursor_obj.execute('''insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')

### Task 4: Query data into the table

statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
print("All the data")
output_all = cursor_obj.fetchall()
for row_all in output_all:
  print(row_all)

## Fetch few rows from the table
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
print("All the data")
# If you want to fetch few rows from the table we use fetchmany(number of rows) and mention the number how many rows you want to fetch
output_many = cursor_obj.fetchmany(2) 
for row_many in output_many:
  print(row_many)

# Fetch only FNAME from the table
statement = '''SELECT FNAME FROM INSTRUCTOR'''
cursor_obj.execute(statement)
print("All the data")
output_column = cursor_obj.fetchall()
for fetch in output_column:
  print(fetch)

## BONUS: now write and execute an update statement that changes the Rav's CITY to MOOSETOWN
query_update='''update INSTRUCTOR set CITY='MOOSETOWN' where FNAME="Rav"'''
cursor_obj.execute(query_update)

statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
print("All the data")
output1 = cursor_obj.fetchmany(2)
for row in output1:
  print(row)

### TASK 5: Retrieve data into Pandas

import pandas as pd
#retrieve the query results into a pandas dataframe
df = pd.read_sql_query("select * from instructor;", conn)
#print the dataframe
df
#print just the LNAME for first row in the pandas data frame
df.LNAME[0]

# Once the data is in a Pandas dataframe, you can do the typical pandas operations on it.
# For example you can use the shape method to see how many rows and columns are in the dataframe
df.shape

### TASK 6: Close the Connection

# We free all resources by closing the connection. 
# Remember that it is always important to close connections so that we can avoid unused connections taking up resources.
conn.close()