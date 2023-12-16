import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
df.head()

# list the data types for each column
print(df.dtypes)

### QUESTION 1: What is the data type of the column "peak-rpm"?
df.dtypes["peak-rpm"]

# For example, we can calculate the correlation between variables  of type "int64" or "float64" using the method "corr":
df.corr()

### QUESTION 2: Find the correlation between the following columns: bore, stroke, compression-ratio, and horsepower
df[["bore","stroke","compression-ratio", "horsepower"]].corr()

# ---------------------------------------------------------------------------------------------------------------------------------- #

##### CONTINUOUS NUMERICAL VARIABLES

## Postive Linear Relationship: Let's find the scatterplot of "engine-size" and "price".
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
plt.show()
# We can examine the correlation between 'engine-size' and 'price'
df[["engine-size", "price"]].corr()

## Negative Linear Relationship: Let's find the scatterplot of "highway-mpg" and "price".
sns.regplot(x="highway-mpg", y="price", data=df)
plt.show()
df[['highway-mpg', 'price']].corr()

## Weak Linear Relationship: Let's see if "peak-rpm" is a predictor variable of "price".
sns.regplot(x="peak-rpm", y="price", data=df)
plt.show()
df[['peak-rpm','price']].corr() # Close to 0, therefore it's a weak relationship

### QUESTION 3: Find the correlation  between x="stroke" and y="price"
sns.regplot(x="stroke", y="price", data=df)
plt.show()
df[["stroke","price"]].corr() # Weak Relationship

## Categorical Variables: Boxplots
# Let's look at the relationship between "body-style" and "price".
sns.boxplot(x="body-style", y="price", data=df)
plt.show()
# We see that the distributions of price between the different body-style categories have a significant overlap, 
# so body-style would not be a good predictor of price. Let's examine engine "engine-location" and "price":
sns.boxplot(x="engine-location", y="price", data=df)
plt.show()
# Here we see that the distribution of price between these two engine-location categories, front and rear, are distinct enough 
# to take engine-location as a potential good predictor of price.
sns.boxplot(x="drive-wheels", y="price", data=df)
plt.show()
# Here we see that the distribution of price between the different drive-wheels categories differs. 
# As such, drive-wheels could potentially be a predictor of price.

# ---------------------------------------------------------------------------------------------------------------------------------- #

##### DESCRIPTIVE STATISTICAL ANALYSIS

# The describe function automatically computes basic statistics for all continuous variables
df.describe()
# We can include type 'objects' as follows:
df.describe(include=['object'])

### Value Counts

df['drive-wheels'].value_counts()
# We can convert the series to a dataframe as follows:
df['drive-wheels'].value_counts().to_frame()

# Let's repeat the above steps but save the results to the dataframe "drive_wheels_counts" and rename the column 
# 'drive-wheels' to 'value_counts'.
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_counts
# Now let's rename the index to 'drive-wheels':
drive_wheels_counts.index.name = 'drive-wheels'
drive_wheels_counts

# engine-location as variable
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
engine_loc_counts.head(10)

# ---------------------------------------------------------------------------------------------------------------------------------- #

##### BASICS OF GROUPING

# The "groupby" method groups data by different categories. 
df['drive-wheels'].unique()
# We can select the columns 'drive-wheels', 'body-style' and 'price', then assign it to the variable "df_group_one"
df_group_one = df[['drive-wheels','body-style','price']]
# We can then calculate the average price for each of the different categories of data.
df_group_one['price'] = pd.to_numeric(df_group_one['price'], errors='coerce')
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False).mean()
df_group_one

# You can also group by multiple variables. 
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
grouped_test1
# This grouped data is much easier to visualize when it is made into a pivot table.
grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
grouped_pivot
# Often, we won't have data for some of the pivot cells. We can fill these missing cells with the value 0, 
# but any other value could potentially be used as well
grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0
grouped_pivot

### QUESTION 4: Use the "groupby" function to find the average "price" of each car based on "body-style"
df_bodystyle = df[['body-style','price']]
grouped_bodystyle = df_bodystyle.groupby(['body-style','price'],as_index=False).mean()
grouped_bodystyle

## Variables: Drive Wheels and Body Style vs. Price

# Let's use a heat map to visualize the relationship between Body Style vs Price.
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()

## The default labels convey no useful information to us. Let's change that:
fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')
# label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index
# move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)
# insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)
# rotate label if too long
plt.xticks(rotation=90)
fig.colorbar(im)
plt.show()

# ---------------------------------------------------------------------------------------------------------------------------------- #

##### CORRELATION AND CAUSATION

# p-value is < 0.001: we say there is strong evidence that the correlation is significant.
# p-value is < 0.05: there is moderate evidence that the correlation is significant.
# p-value is < 0.1: there is weak evidence that the correlation is significant.
# p-value is > 0.1: there is no evidence that the correlation is significant.

## We can calculate the Pearson Correlation of the of the 'int64' or 'float64'  variables
df.corr()

## P-value: probability value that the correlation between these two variables is statistically significant
from scipy import stats

# Wheel-Base vs. Price
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

# Horse-power vs. Price
pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

# Length vs. Price
pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)  

# Width vs. Price
pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value ) 

# Curb-Weight vs. Price
pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)  

# Engine-Size vs. Price
pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value) 

# Bore vs. Price
pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =  ", p_value ) 

# City-mpg vs. Price
pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)  

# Highway-mpg vs. Price
pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value ) 

# ---------------------------------------------------------------------------------------------------------------------------------- #

##### ANOVA

## ANOVA returns two parameters: F-test score and P-value

## Drive Wheels

# The ANOVA algorithm averages the data automatically, we do not need to take the average before hand.
grouped_test2=df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
grouped_test2.head(2)
df_gptest
grouped_test2.get_group('4wd')['price']

## ANOVA: We can use the function 'f_oneway' in the module 'stats' to obtain the F-test score and P-value.
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'], grouped_test2.get_group('4wd')['price'])  
print("ANOVA results: F=", f_val, ", P =", p_val)

# This is a great result with a large F-test score showing a strong correlation and a P-value of almost 0 implying almost 
# certain statistical significance. But does this mean all three tested groups are all this highly correlated? 
# Let's examine them separately.

## fwd and rwd
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'])  
print( "ANOVA results: F=", f_val, ", P =", p_val)

## 4wd and fwd
f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('fwd')['price'])
print("ANOVA results: F=", f_val, ", P =", p_val) # P-value > 0.1 therefore not statistically significant 