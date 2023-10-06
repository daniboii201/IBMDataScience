# !pip install pandas==1.3.3
# !pip install requests==2.26.0
# !mamba install bs4==4.10.0 -y
# !mamba install html5lib==1.1 -y 
# !pip install lxml==4.6.4
# !pip install plotly==5.3.1
import pandas as pd
import requests
from bs4 import BeautifulSoup

## Step 1: Send an HTTP request to the webpage using the requests library.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data  = requests.get(url).text

## Step 2: Parse the HTML content

### How to parse the data using Beautiful soup library?
# The HTML or XML content that you want to parse as a string
# The name of the parser that you want to use to parse the HTML or XML content
soup = BeautifulSoup(data, 'html5lib')

## Step 3: Identify the HTML tags
netflix_data_list = []

## Step 4: Use Beautiful soup method for extracting data
# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    # Finally we append the data of each row to the table
    new_row = {
        "Date": date,
        "Open": Open,
        "High": high,
        "Low": low,
        "Close": close,
        "Adj Close": adj_close,
        "Volume": volume
    }
    netflix_data_list.append(new_row)
netflix_data = pd.DataFrame(netflix_data_list)

### Step 5: Print the Extracted Data
netflix_data.head()

##### Extracting data using pandas library

# We can also use the pandas read_html function from pandas library and use the URL for extracting data.
read_html_pandas_data = pd.read_html(url)
# Or we can convert the BeautifulSoup object to a string
read_html_pandas_data = pd.read_html(str(soup)) # FutureWarning: Passing literal html to 'read_html' is deprecated and will be removed in a future version.
# Because there is only one table on the page, we just take the first table in the list returned
netflix_dataframe = read_html_pandas_data[0]
netflix_dataframe.head()

### Using Webscraping to Extract Stock Data Exercise

url3 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html'
html_data = requests.get(url3).text
souphtml = BeautifulSoup(html_data,'html5lib')

# Question 1: What is the content of the title attribute?
title_element = souphtml.find('title')
title_element

# Using beautiful soup extract the table with historical share prices and store it into a dataframe named amazon_data. 
# The dataframe should have columns Date, Open, High, Low, Close, Adj Close, and Volume. 
# Fill in each variable with the correct data from the list col.
amazon_data_list = []

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    new_row2 = {
        "Date": date,
        "Open": Open,
        "High": high,
        "Low": low,
        "Close": close,
        "Adj Close": adj_close,
        "Volume": volume
    }
    amazon_data_list.append(new_row2)
amazon_data = pd.DataFrame(amazon_data_list)

# Question 1: Print out the first five rows of the amazon_data dataframe you created.
amazon_data.head()
# Question 2: What is the name of the columns of the dataframe?
column_names = amazon_data.columns
column_names
# Question 3: What is the Open of the last row of the amazon_data dataframe?
last_row_open = amazon_data.iloc[-1]['Open']
last_row_open