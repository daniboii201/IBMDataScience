# Create a python list
a = ["0", 1, "two", "3", 4]
# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])
# import numpy library
import numpy as np
# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
a
# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])
# Checking NumPy Version
print(np.__version__)
# Check the type of the array
type(a)
# Check the type of the values stored in numpy array
a.dtype

# Try it yourself
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
type(b)
b.dtype

# Create numpy array
c = np.array([20, 1, 2, 3, 4])
c
# Assign the first element to 100
c[0] = 100
c
# Assign the 5th element to 0
c[4] = 0
c

# Try it yourself
a = np.array([10, 2, 30, 40,50])
a[1]=20
a

# Slicing the numpy array
d = c[1:4]
d
# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400
c
# We can also define the steps in slicing, like this: [start:end:step]
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])
# If we don't pass start its considered 0
print(arr[:4])
# If we don't pass end it considers till the length of array.
print(arr[4:])
# If we don't pass step its considered 1
print(arr[1:5:])

# Try it yourself. Print the even elements in the given array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[::2])

### Assign Value with List
# Create the index list
select = [0, 2, 3, 4]
select
# Use List to select elements
d = c[select]
d
# Assign the specified elements to new value
c[select] = 100000
c

### Other Attributes
# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
a
# Get the size of numpy array
a.size
# Get the number of dimensions of numpy array
a.ndim
# Get the shape/size of numpy array
a.shape

# Try it yourself. Find the size, dimension and shape for the given array b
b = np.array([10, 20, 30, 40, 50, 60, 70])
b.size
b.ndim
b.shape

# Numpy Statistical Functions
# Create a numpy array
a = np.array([1, -1, 1, -1])
# Get the mean of numpy array
mean = a.mean()
mean
# Get the standard deviation of numpy array
standard_deviation=a.std()
standard_deviation
# Create a numpy array
b = np.array([-1, 2, 3, 4, 5])
b
# Get the biggest value in the numpy array
max_b = b.max()
max_b
# Get the smallest value in the numpy array
min_b = b.min()
min_b

# Try it yourself. Find the sum of maximum and minimum value in the given numpy array
c = np.array([-10, 201, 43, 94, 502])
max_c = c.max()
max_c
min_c = c.min()
min_c

### Numpy Array Operations
## Array Addition
# Consider the numpy array u:
u = np.array([1, 0])
u
# Consider the numpy array v:
v = np.array([0, 1])
v
# We can add the two arrays and assign it to z:
z = np.add(u, v)
z
# The operation is equivalent to vector addition:
import time 
import sys
import numpy as np 
import matplotlib.pyplot as plt
def Plotvec1(u, z, v):
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1) # Add an arrow to the U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u') # Adds the text u to the Axes 
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1) # Add an arrow to the v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v') # Adds the text v to the Axes 
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z') # Adds the text z to the Axes 
    plt.ylim(-2, 2) # set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2) # set the xlim to left(-2), right(2)
# Plot numpy arrays
Plotvec1(u, z, v) 

# Try it yourself. Perform addition operation on the given numpy array arr1 and arr2:
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr3 = np.add(arr1, arr2)
arr3

## Array Subtraction
# Consider the numpy array a:
a = np.array([10, 20, 30])
a
# Consider the numpy array b:
b = np.array([5, 10, 15])
b   
# We can subtract the two arrays and assign it to c:
c = np.subtract(a, b)
print(c)

# Try it yourself. Perform subtraction operation on the given numpy array arr1 and arr2:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr3 = np.subtract(arr1,arr2)
arr3

### Array Multiplication
# Consider the vector numpy array y:
x = np.array([1, 2])
x
y = np.array([2, 1])
y
# We can multiply every element in the array by 2:
z = np.multiply(x, y)
z

# Try it yourself. Perform multiply operation on the given numpy array arr1 and arr2:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([2, 1, 2, 3, 4, 5])
arr3 = np.multiply(arr1,arr2)
arr3

### Array Division
# Consider the vector numpy array a:
a = np.array([10, 20, 30])
a
# Consider the vector numpy array b:
b = np.array([2, 10, 5])
b
# We can divide the two arrays and assign it to c:
c = np.divide(a, b)
c

# Try it yourself. Perform division operation on the given numpy array arr1 and arr2:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])
arr3 = np.divide(arr1,arr2)
arr3

### Dot product
# The dot product of the two numpy arrays u and v is given by:
X = np.array([1, 2])
Y = np.array([3, 2])
# Calculate the dot product
np.dot(X, Y)
#Elements of X
print(X[0])
print(X[1])
#Elements of Y
print(Y[0])
print(Y[1])

# Try it yourself. Perform dot operation on the given numpy array ar1 and ar2:
arr1 = np.array([3, 5])
arr2 = np.array([2, 4])
arr3 = np.dot(arr1,arr2)
arr3

### Adding Constant to a Numpy Array
# Consider the following array:
u = np.array([1, 2, 3, -1]) 
u
# Adding the constant 1 to each element in the array:
u + 1

# Try it yourself. Add Constant 5 to the given numpy array ar:
arr = np.array([1, 2, 3, -1]) 
arr2 = arr + 5
arr2

### Mathematical Functions
# We can access the value of pi in numpy as follows:
np.pi
# We can create the following numpy array in Radians:
x = np.array([0, np.pi/2 , np.pi])
# We can apply the function sin to the array x and assign the values to the array y; this applies the sine function to each element in the array:
y = np.sin(x)
y

### Linspace
## A useful function for plotting mathematical functions is linspace. Linspace returns evenly spaced numbers over a specified interval.
## numpy.linspace(start, stop, num = int value)
## start : start of interval range
## stop : end of interval range
## num : Number of samples to generate.

# Makeup a numpy array within [-2, 2] and 5 elements
np.linspace(-2, 2, num=5)
# If we change the parameter num to 9, we get 9 evenly spaced numbers over the interval from -2 to 2:
np.linspace(-2, 2, num=9)
# We can use the function linspace to generate 100 evenly spaced samples from the interval 0 to 2π:
x = np.linspace(0, 2*np.pi, num=100)
# Calculate the sine of x list
y = np.sin(x)
# Plot the result
plt.plot(x, y)

# Try it yourself. Make a numpy array within [5, 4] and 6 elements:
np.linspace(5,4,num=6)

### Iterating 1-D Arrays
## Iterating means going through elements one by one.
## If we iterate on a 1-D array it will go through each element one by one.

# If we execute the numpy array, we get in the array format
arr1 = np.array([1, 2, 3])
print(arr1)
# But if you want to result in the form of the list, then you can use for loop:
for x in arr1:
  print(x)

######################### QUIZ: 1D Numpy Array #########################

# Implement the following vector subtraction in numpy: u-v
u = np.array([1, 0])
v = np.array([0, 1])
np.subtract(u,v)
u-v
# Multiply the numpy array z with -2:
z = np.array([2, 4])
np.multiply(-2,z)
# Consider the list [1, 2, 3, 4, 5] and [1, 0, 1, 0, 1]. Cast both lists to a numpy array then multiply them together:
x = np.array([1,2,3,4,5])
y = np.array([1,0,1,0,1])
np.multiply(x,y)

# Convert the list [-1, 1] and [1, 1] to numpy arrays a and b. Then, plot the arrays as vectors using the fuction Plotvec2 and find their dot product:
a = np.array([-1, 1])
b = np.array([1, 1])
print("The dot product is", np.dot(a,b))
## EXPLANATION: The vectors used are perpendicular. As a result, the dot product is zero. 

# Convert the list [1, 2, 3] and [8, 9, 10] to numpy arrays arr1 and arr2. 
# Then perform Addition , Subtraction , Multiplication , Division and Dot Operation on the arr1 and arr2.
arr1 = np.array([1,2,3])
arr2 = np.array([8,9,10])
arradd = np.add(arr1,arr2)
arrsub = np.subtract(arr1,arr2)
arrmult = np.multiply(arr1,arr2)
arrdiv = np.divide(arr1,arr2)
arrdot = np.dot(arr1,arr2)
arradd
arrsub
arrmult
arrdiv
arrdot

# Convert the list [1, 2, 3, 4, 5] and [6, 7, 8, 9, 10] to numpy arrays arr1 and arr2. Then find the even and odd numbers from arr1 and arr2.
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
arreven1 = arr1[1:5:2] # arr1 starts with an odd number
arrodd1 = arr1[0:5:2] 
arreven2 = arr2[0:5:2] # arr2 starts with an even number
arrodd2 = arr2[1:5:2]
arreven1
arrodd1
arreven2
arrodd2

######################### END OF QUIZ #########################