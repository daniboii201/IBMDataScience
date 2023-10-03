### CREATE A 2D NUMPY ARRAY

# Import the libraries
import numpy as np 
import matplotlib.pyplot as plt
# Consider the list a, which contains three nested lists each of equal size.
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a
# Convert list to Numpy Array
# Every element is the same type
A = np.array(a)
A
# We can use the attribute ndim to obtain the number of axes or dimensions, referred to as the rank.
A.ndim
# Attribute shape returns a tuple corresponding to the size or number of each dimension.
A.shape
# The total number of elements in the array is given by the attribute size.
A.size

### Accessing different elements of a Numpy Array

# Access the element on the second row and third column
A[1, 2]
# Access the element on the second row and third column
A[1][2]
# Access the element on the first row and first column
A[0][0]
# Access the element on the first row and first and second columns
A[0][0:2]
# Access the element on the first and second rows and third column
A[0:2, 2]

### Basic Operations

# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
X
# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
Y
# We can add the numpy arrays as follows.
Z = X + Y
Z

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
Y
# Multiply Y with 2
Z = 2 * Y
Z

# We can perform element-wise product of the array X and Y as follows:
# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
Y
# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
X
# Multiply X with Y
Z = X * Y
Z

# We can also perform matrix multiplication with the numpy arrays A and B as follows:
# First, we define matrix A and B:
# Create a matrix A
A = np.array([[0, 1, 1], [1, 0, 1]])
A
# Create a matrix B
B = np.array([[1, 1], [1, 1], [-1, 1]])
B
# We use the numpy function dot to multiply the arrays together.
Z = np.dot(A,B)
Z
np.sin(Z)

# We use the numpy attribute T to calculate the transposed matrix
# Create a matrix C
C = np.array([[1,1],[2,2],[3,3]])
C
# Get the transposed of C
C.T

######################### QUIZ: 2D Numpy Array #########################

# Consider the following list a, convert it to Numpy Array.
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
A = np.array(a)
A
# Calculate the numpy array size.
A.size
# Access the element on the first row and first and second columns.
A[0]
A[0:2]
# Perform matrix multiplication with the numpy arrays A and B.
B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])
B
AB = np.dot(A,B)
AB

######################### END OF QUIZ #########################