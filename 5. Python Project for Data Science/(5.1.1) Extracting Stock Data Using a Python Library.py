# !pip install yfinance==0.2.4
# !pip install pandas==1.3.3
import yfinance as yf
import pandas as pd
import requests
import matplotlib.pyplot as plt
import json

##### Using the yfinance Library to Extract Stock Data

# Using the Ticker module we can create an object that will allow us to access functions to extract data. 
# To do this we need to provide the ticker symbol for the stock, here the company is Apple and the ticker symbol is AAPL.
apple = yf.Ticker("AAPL")
# Now we can access functions and variables to extract the type of data we need.
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json'
response = requests.get(url)
if response.status_code == 200:
    with open("apple.json", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")

## Stock info
# Using the attribute info we can extract information about the stock as a Python dictionary.
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
apple_info
# We can get the 'country' using the key country
apple_info['country']

## Extracting Share Price

# A share is the single smallest part of a company's stock that you can buy, the prices of these shares fluctuate over time. 
# Using the history() method we can get the share price of the stock over a certain period of time. 
# Using the period parameter we can set how far back from the present to get data. 
# The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.
apple_share_price_data = apple.history(period="max")

# The format that the data is returned in is a Pandas DataFrame. 
# With the Date as the index the share Open, High, Low, Close, Volume, and Stock Splits are given for each day.
apple_share_price_data.head()

# We can reset the index of the DataFrame with the reset_index function. 
# We also set the inplace paramter to True so the change takes place to the DataFrame itself.
apple_share_price_data.reset_index(inplace=True)

# We can plot the Open price against the Date:
apple_share_price_data.plot(x="Date", y="Open")
plt.show()

### Extracting Dividends

# Dividends are the distribution of a companys profits to shareholders. 
# In this case they are defined as an amount of money returned per share an investor owns. 
# Using the variable dividends we can get a dataframe of the data. 
# The period of the data is given by the period defined in the 'history` function.
apple.dividends
# We can plot the dividends overtime:
apple.dividends.plot()
plt.show()

################################# Exercise #################################

# Now using the Ticker module create an object for AMD (Advanced Micro Devices) with the ticker symbol is AMD called; name the object amd.

amd = yf.Ticker("AMD")

url2 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json'
response = requests.get(url2)
if response.status_code == 200:
    with open("amd.json", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print("Failed to download the file. Status code: {response.status_code}")

with open("amd.json") as json_file:
    amd_info = json.load(json_file)
    # Print the type of data variable    
    print("Type:", type(apple_info))
amd_info

### Question 1 Use the key 'country' to find the country the stock belongs to.
amd_country = amd_info['country']
amd_country

### Question 2 Use the key 'sector' to find the sector the stock belongs to.
amd_sector = amd_info['sector']
amd_sector

### Question 3 Obtain stock data for AMD using the history function, set the period to max. Find the Volume traded on the first day (first row).
amd_stock_data = amd.history(period="max")
first_day_volume = amd_stock_data.iloc[0]['Volume']
print("Volume traded on the first day:", int(first_day_volume))

################################# END OF EXERCISE #################################