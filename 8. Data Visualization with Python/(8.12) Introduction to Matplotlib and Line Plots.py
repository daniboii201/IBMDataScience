import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
import matplotlib as mpl
import matplotlib.pyplot as plt

df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')
print('Data read into a pandas dataframe!')

# Let's view the top 5 rows of the dataset using the `head()` function.
df_can.head()
# Let's set Country as the index, it will help you to plot the charts easily, by refering to the country names as index value
df_can.set_index('Country', inplace=True)
#let's check
df_can.head(3)
# optional: to remove the name of the index
df_can.index.name = None
# useful for plotting later on
years = list(map(str, range(1980, 2014)))
years

##### Matplotlib.pyplot #####

print(plt.style.available)
mpl.style.use(['ggplot']) # optional: for ggplot-like style

##### Line Pots (Series/Dataframe) #####

### Case Study

#Since we converted the years to string, 
#let's declare a variable that will allow us to easily call upon the full range of years:
years = list(map(str, range(1980, 2014)))
#creating data series
haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
haiti.head()
# Next, we will plot a line plot by appending `.plot()` to the `haiti` dataframe.
haiti.plot()
# pandas automatically populated the x-axis with the index values (years), and the y-axis with the column values (population).
haiti.plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show() # need this line to show the updates made to the figure

plt.text(2000, 6000, '2010 Earthquake') # years stored as type int
plt.text(20, 6000, '2010 Earthquake') # years stored as type int


##### Question: Let's compare the number of immigrants from India and China from 1980 to 2013.
### Step 1: Get the data set for China and India, and display the dataframe.
df_CI = df_can.loc[['India', 'China'], years]
df_CI
### Step 2: Plot graph. We will explicitly specify line plot by passing in `kind` parameter to `plot()`.
df_CI.plot(kind='line')

df_CI.index = df_CI.index.map(int) # let's change the index values of df_CI to type integer for plotting
df_CI.plot(kind='line')
plt.title('Immigrants from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()

##### Question: Compare the trend of top 5 countries that contributed the most to immigration to Canada. #####

# Step 1: Get the dataset. Recall that we created a Total column that calculates cumulative immigration by country. 
# We will sort on this column to get our top 5 countries using pandas sort_values() method.
inplace = True # paramemter saves the changes to the original df_can dataframe
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
# get the top 5 entries
df_top5 = df_can.head(5)
# transpose the dataframe
df_top5 = df_top5[years].transpose() 
print(df_top5)

# Step 2: Plot the dataframe. To make the plot more readeable, we will change the size using the `figsize` parameter.
df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size
plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()