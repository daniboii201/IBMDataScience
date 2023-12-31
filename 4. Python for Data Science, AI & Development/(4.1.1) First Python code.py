# Try your first Python output
print('Hello, Python!')

# Check the Python Version
import sys
print(sys.version)

# Practice on writing comments
print('Hello, Python!') # This line prints a string
# print('Hi')

# Print string as error message
frint("Hello, Python!")
# The error message tells you: where the error occurred (more useful in large notebook cells or scripts), and what kind of error it was (NameError)

# Try to see built-in error message
print("Hello, Python!)
      
# Print string and error to see the running order
print("This will be printed")
frint("This will cause an error")
print("This will NOT be printed")

######################### EXERCISE 1: Your First Program #########################

print("Hello World!") # Print the traditional hello world

######################### END OF EXERCISE 1 #########################

# Integer
11

# Float
2.14

# String
"Hello, Python 101!"

# Type of 12
type(12)
# Type of 2.14
type(2.14)
# Type of "Hello, Python 101!"
type("Hello, Python 101!")
# Type of 12.0
type(12.0)

# Print the type of -1
type(-1)
# Print the type of 4
type(4)
# Print the type of 0
type(0)

# Print the type of 1.0
type(1.0) # Notice that 1 is an int, and 1.0 is a float
# Print the type of 0.5
type(0.5)
# Print the type of 0.56
type(0.56)
# System settings about float type
sys.float_info

# Verify that this is an integer
type(2)
# Convert 2 to a float
float(2)
# Convert integer 2 to a float and check its type
type(float(2))

# Casting 1.1 to integer will result in loss of information
int(1.1)
# Convert a string into an integer
int('1')
# Convert a string into an integer with error
int('1 or 2 people')
# Convert the string "1.2" into a float
float('1.2')

# Convert an integer to a string
str(1)
# Convert a float to a string
str(1.2)

# Value true
True
# Value false
False

# Type of True
type(True)
# Type of False
type(False)

# Convert True to int
int(True)
# Convert 1 to boolean
bool(1)
# Convert 0 to boolean
bool(0)
# Convert True to float
float(True)

######################### EXERCISE 2: Types #########################

type(6/2) # float
type(6//2) # int, as the double slashes stand for integer division 

######################### END OF EXERCISE 2 #########################

# Addition operation expression
43 + 60 + 16 + 41
# Subtraction operation expression
50 - 60
# Multiplication operation expression
5 * 5
# Division operation expression
25 / 5
# Division operation expression
25 / 6
# Integer division operation expression
25 // 5
# Integer division operation expression
25 // 6

######################### EXERCISE 3: Expression #########################

160/60 
# Or 
160//60

######################### END OF EXERCISE 3 #########################

# Mathematical expression
30 + 2 * 60
# Mathematical expression
(30 + 2) * 60

# Store value into variable
x = 43 + 60 + 16 + 41
# Print out the value in variable
x

# Use another variable to store the result of the operation between variable and value
y = x / 60
y

# Overwrite variable with new value
x = x / 60
x

# Name the variables meaningfully
total_min = 43 + 42 + 57 # Total length of albums in minutes
total_min

# Name the variables meaningfully
total_hours = total_min / 60 # Total length of albums in hours 
total_hours

# Complicate expression
total_hours = (43 + 42 + 57) / 60  # Total hours in a single expression
total_hours

######################### EXERCISE 4: Expression and Variables in Python #########################

x = 3 + 2 * 2
y = (3 + 2) * 2
z = x + y

######################### END OF EXERCISE 4 #########################