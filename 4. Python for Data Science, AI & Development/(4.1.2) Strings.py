# Use quotation marks for defining string
"Michael Jackson"

# Use single quotation marks for defining string
'Michael Jackson'

# Digitals and spaces in string
'1 2 3 4 5 6 '

# Special characters in string
'@#2_#]&*^%$'

# Print the string
print("hello!")

# Assign string to variable
name = "Michael Jackson"
name

# --------------------------------------------------------------------#

### Indexing

# Print the first element in the string
print(name[0])
# Print the element on index 6 in the string
print(name[6])
# Print the element on the 13th index in the string
print(name[13])

# --------------------------------------------------------------------#

### Negative Indexing

# Print the last element in the string
print(name[-1])
# Print the first element in the string
print(name[-15])
# Find the length of string
len("Michael Jackson")

# --------------------------------------------------------------------#

### Slicing

# Take the slice on variable name with only index 0 to index 3
name[0:4]
# Take the slice on variable name with only index 8 to index 11
name[8:12]

# --------------------------------------------------------------------#

### Stride

# Get every second element. The elments on index 1, 3, 5 ...
name[::2]
# Get every second element in the range from index 0 to index 4
name[0:5:2]

# --------------------------------------------------------------------#

### Concatenate Strings

# Concatenate two strings
statement = name + "is the best"
statement

# Print the string for 3 times
3 * "Michael Jackson"

# Concatenate strings
name = "Michael Jackson"
name = name + " is the best"
name

# --------------------------------------------------------------------#

### Escape Sequences

# New line escape sequence
print(" Michael Jackson \n is the best" )
# Tab escape sequence
print(" Michael Jackson \t is the best" )
# Include back slash in string
print(" Michael Jackson \\ is the best" )
# r will tell python that string will be display as raw string
print(r" Michael Jackson \ is the best" )

# --------------------------------------------------------------------#

### String Operations

# Convert all the characters in string to upper case
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)

# Replace the old substring with the new target substring is the segment has been found in the string
a = "Michael Jackson is the best"
b = a.replace('Michael', 'Janet')
b

# Find the substring in the string. Only the index of the first elment of substring in string will be the output
name = "Michael Jackson"
name.find('el')

# Find the substring in the string.
name.find('Jack')

# If cannot find the substring in the string
name.find('Jasdfasdasdf')

######################### QUIZ: Strings #########################

# What is the value of the variable a after the following code is executed?
a = "1"

# What is the value of the variable b after the following code is executed?
b = "2"

# What is the value of the variable c after the following code is executed?
c = a + b

# Consider the variable d use slicing to print out the first three elements
d = "ABCDEFG"
print(d[:3]) 
# or 
print(d[0:3])

# Use a stride value of 2 to print out every second character of the string e:
e = 'clocrkr1e1c1t'
print(e[::2])

# Print out a backslash:
print(r"\\\\\\ ")
# or
print(r"\ ")

# Convert the variable f to uppercase:
f = "You are wrong"
f.upper()

# Consider the variable g, and find the first index of the sub-string snow:
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
g.find("snow")

# In the variable g, replace the sub-string Mary with Bob:
g.replace("Mary","Bob")

######################### END OF QUIZ #########################