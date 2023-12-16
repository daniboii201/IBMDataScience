import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
df.head()

# Let's load the modules for linear regression
from sklearn.linear_model import LinearRegression

# ---------------------------------------------------------------------------------------------------------------------------------- #

##### SIMPLE LINEAR REGRESSION

# Create the linear regression object
lm = LinearRegression()
lm

# How could 'highway-mpg' help us predict car price?
X = df[['highway-mpg']]
Y = df['price']
# Fit the linear model using highway-mpg (intercept and slope):
lm.fit(X,Y)
# We can output a prediction:
Yhat=lm.predict(X)
Yhat[0:5]
# What is the value of the intercept (a)?
lm.intercept_
# What is the value for the slope (b)?
lm.coef_

### QUESTION 1
# a) Create a linear regression object called "lm1".
lm1 = LinearRegression()
lm1
# b) Train the model using "engine-size" as the independent variable and "price" as the dependent variable
lm1.fit(df[['engine-size']], df[['price']])
lm1
# c) Find the slope and intercept of the model
lm1.intercept_
lm1.coef_
# d) What is the equation of the predicted line? You can use x and yhat or "engine-size" or "price"
Yhat = (lm1.intercept_) + (lm1.coef_*X)

##### MULTIPLE LINEAR REGRESSION

## Yhat = a + b1X1 + b2X2 + b3X3 + b4X4

# Let's develop a model using these variables as the predictor variables.
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
# Fit the linear model using the four above-mentioned variables.
lm.fit(Z, df['price'])
# What is the value of the intercept(a)?
lm.intercept_
# What are the values of the coefficients (b1, b2, b3, b4)?
lm.coef_

### QUESTION 2:
# a) Create and train a Multiple Linear Regression model "lm2" where the response variable is "price", and the predictor 
# variable is "normalized-losses" and  "highway-mpg".
lm2 = LinearRegression()
Z2 = df[['normalized-losses','highway-mpg']]
lm2.fit(Z2, df['price'])
# b) Find the coefficient of the model
lm2.coef_

# ---------------------------------------------------------------------------------------------------------------------------------- #

##### MODEL EVALUATION USING VISUALIZATION

import seaborn as sns
import matplotlib.pyplot as plt

## Regression Plot

# Let's visualize **highway-mpg** as potential predictor variable of price:
width = 12
height = 10
plt.figure(figsize=(width, height))
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)
plt.show()

# We can see from this plot that price is negatively correlated to highway-mpg since the regression slope is negative.
# One thing to keep in mind when looking at a regression plot is to pay attention to how scattered the data points are around 
# the regression line. This will give you a good indication of the variance of the data and whether a linear model would be the 
# best fit or not. If the data is too far off from the line, this linear model might not be the best model for this data.
# Let's compare this plot to the regression plot of "peak-rpm".

plt.figure(figsize=(width, height))
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)
plt.show()

# Comparing the regression plot of "peak-rpm" and "highway-mpg", we see that the points for "highway-mpg" are much closer 
# to the generated line and, on average, decrease. The points for "peak-rpm" have more spread around the predicted line and 
# it is much harder to determine if the points are decreasing or increasing as the "peak-rpm" increases.

### QUESTION 3: Given the regression plots above, is "peak-rpm" or "highway-mpg" more strongly correlated with "price"? 
# Use the method  ".corr()" to verify your answer.
sns.regplot(x="peak-rpm", y="price", data=df)
plt.show()
df[["peak-rpm", "price"]].corr()
sns.regplot(x="highway-mpg", y="price", data=df)
plt.show()
df[["highway-mpg", "price"]].corr()
# "highway-mpg" has a stronger correlation with "price"

##### RESIDUAL PLOT

## Residual Plot
# A good way to visualize the variance of the data is to use a residual plot.
# What is a residual?
# The difference between the observed value (y) and the predicted value (Yhat) is called the residual (e). When we look at a regression plot, the residual is the distance from the data point to the fitted regression line.
# So what is a residual plot?
# A residual plot is a graph that shows the residuals on the vertical y-axis and the independent variable on the horizontal x-axis.
# What do we pay attention to when looking at a residual plot?
# We look at the spread of the residuals:
# If the points in a residual plot are randomly spread out around the x-axis, then a linear model is appropriate for the data.
# Why is that? Randomly spread out residuals means that the variance is constant, and thus the linear model is a good fit for this data
width = 12
height = 10
plt.figure(figsize=(width, height))
sns.residplot(x=df['highway-mpg'], y=df['price'])
plt.show()
## What is this plot telling us?
# We can see from this residual plot that the residuals are not randomly spread around the x-axis, leading us to believe that maybe 
# a non-linear model is more appropriate for this data.

##### MULTIPLE LINEAR REGRESSION

# How do we visualize a model for Multiple Linear Regression? This gets a bit more complicated because you can't visualize it 
# with regression or residual plot.
# One way to look at the fit of the model is by looking at the distribution plot. We can look at the distribution of the fitted
# values that result from the model and compare it to the distribution of the actual values.

# First, let's make a prediction:
Y_hat = lm.predict(Z)
plt.figure(figsize=(width, height))
#
ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)
#
plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')
#
plt.show()
plt.close()

# ---------------------------------------------------------------------------------------------------------------------------------- #

##### POLYNOMIAL REGRESSION AND PIPELINES

# Polynomial regression is a particular case of the general linear regression model or multiple linear regression models.
# We get non-linear relationships by squaring or setting higher-order terms of the predictor variables. 
# There are different orders of polynomial regression: Quadratic, Cubic and Higher-Order

# We will use the following function to plot the data:
def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)
    #
    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')
    #
    plt.show()
    plt.close()

# Let's get the variables:
x = df['highway-mpg']
y = df['price']
# Let's fit the polynomial using the function polyfit, then use the function poly1d to display the polynomial function.
# Here we use a polynomial of the 3rd order (cubic) 
f = np.polyfit(x, y, 3)
p = np.poly1d(f)
print(p)
# Let's plot the function
PlotPolly(p, x, y, 'highway-mpg')
np.polyfit(x, y, 3)

### QUESTION 4: Create 11 order polynomial model with the variables x and y from above.
f1 = np.polyfit(x,y,11)
p1 = np.poly1d(f1)
print(p1)
PlotPolly(p1,x,y, 'Highway MPG')

# We can perform a polynomial transform on multiple features. First, we import the module: 
from sklearn.preprocessing import PolynomialFeatures
