import pandas as pd
import matplotlib.pylab as plt
import numpy as np
from matplotlib import pyplot

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df = pd.read_csv(filename, names = headers)
# To see what the data set looks like, we'll use the head() method.
df.head()

##### IDENTIFY AND HANDLE MISSING VALUES

# replace "?" to NaN
df.replace("?", np.nan, inplace = True)
df.head(5)

## Evaluating for Missing Data
# .isnull() [Null values = True]
# .isnotnull() [Null values = False]
missing_data = df.isnull()
missing_data.head(5)

## Count missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    

# Calculate the mean value for the "normalized-losses" column
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)

# Replace "NaN" with mean value in "normalized-losses" column
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

# Calculate the mean value for the "bore" column
avg_bore=df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)

# Replace "NaN" with the mean value in the "bore" column
df["bore"].replace(np.nan, avg_bore, inplace=True)

### QUESTION 1: Based on the example above, replace NaN in "stroke" column with the mean value
avg_stroke = df['stroke'].astype('float').mean(axis=0) 
df["stroke"].replace(np.nan, avg_stroke, inplace=True)

# Calculate the mean value for the "horsepower" column
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)

# Replace "NaN" with the mean value in the "horsepower" column
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

# Calculate the mean value for "peak-rpm" column
avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)

# Replace "NaN" with the mean value in the "peak-rpm" column
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

# To see which values are present in a particular column, we can use the ".value_counts()" method:
df['num-of-doors'].value_counts()

# You can see that four doors is the most common type. We can also use the ".idxmax()" method to calculate the most common type 
# automatically:
df['num-of-doors'].value_counts().idxmax()

# The replacement procedure is very similar to what you have seen previously:
df["num-of-doors"].replace(np.nan, "four", inplace=True)

# Finally, drop all rows that do not have price data:
# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)
# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)
df.head()

### Correct Data Format
# df.dtypes()
# df.astype()

# Convert data types to proper format
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
df.dtypes

##### DATA STANDARIZATION

df.head()
# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-L/100km'] = 235/df["city-mpg"]
# check your transformed data 
df.head()

### QUESTION 2: According to the example above, transform mpg to L/100km in the column of "highway-mpg" and change the 
# name of column to "highway-L/100km"
df.rename(columns={'"highway-mpg"':'highway-L/100km'}, inplace=True)

##### DATA NORMALIZATION

# To demonstrate normalization, say you want to scale the columns "length", "width" and "height".
# Target: normalize those variables so their value ranges from 0 to 1
# Approach: replace the original value by (original value)/(maximum value)
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()

### QUESTION 3: According to the example above, normalize the column "height"
df['height'] = df['height']/df['height'].max()
# show the scaled columns
df[["length","width","height"]].head()


##### BINNING

### Example of Binning Data in Pandas
# Convert data to correct format
df["horsepower"]=df["horsepower"].astype(int, copy=True)
# Plot the histogram of horsepower to see the distribution of horsepower.
import matplotlib.pyplot as plt
plt.hist(df["horsepower"])
# set x/y labels and plot title
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")

# Build a bin array with a minimum value to a maximum value by using the bandwidth calculated above. 
# The values will determine when one bin ends and another begins.
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
bins
# Set group names
group_names = ['Low', 'Medium', 'High']
# Apply the function "cut" to determine what each value of `df['horsepower']` belongs to. 
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
df[['horsepower','horsepower-binned']].head(20)
# See the number of vehicles in each bin:
df["horsepower-binned"].value_counts()
# Plot the distribution of each bin:
pyplot.bar(group_names, df["horsepower-binned"].value_counts())
# set x/y labels and plot title
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")

### BINS VISUALIZATION
# Normally, you use a histogram to visualize the distribution of bins we created above.

# draw historgram of attribute "horsepower" with bins = 3
plt.hist(df["horsepower"], bins = 3)
# set x/y labels and plot title
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")
plt.show()

### Indicator Variable (or Dummy Variable)

df.columns
# Get the indicator variables and assign it to data frame "dummy_variable_1":
dummy_variable_1 = pd.get_dummies(df["fuel-type"])
dummy_variable_1.head()
# Change the column names for clarity:
dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)
dummy_variable_1.head()
# In the data frame, column 'fuel-type' now has values for 'gas' and 'diesel' as 0s and 1s.
# merge data frame "df" and "dummy_variable_1" 
df = pd.concat([df, dummy_variable_1], axis=1)
# drop original column "fuel-type" from "df"
df.drop("fuel-type", axis = 1, inplace=True)
df.head()

### QUESTION 4: Similar to before, create an indicator variable for the column "aspiration"
dummy_variable_2 = pd.get_dummies(df['aspiration'])
dummy_variable_2.rename(columns={'std':'aspiration-std', 'turbo': 'aspiration-turbo'}, inplace=True)
dummy_variable_2.head()

### QUESTION 5: Merge the new dataframe to the original dataframe, then drop the column 'aspiration'
df2 = pd.concat([df,dummy_variable_2], axis=1)
df2.drop('aspiration', axis = 1, inplace=True)

# Save the new csv
df.to_csv('clean_df.csv')