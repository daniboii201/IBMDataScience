# Create a list
L = ["Michael Jackson", 10.1, 1982]
L

# Print the elements on each index
print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )

# Sample List
["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]

# Sample List
L = ["Michael Jackson", 10.1,1982,"MJ",1]
L
# List slicing
L[3:5]

# Use extend to add elements to list
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L

# Use append to add elements to list
L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
L

# Use extend to add elements to list
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L
# Use append to add elements to list
L.append(['a','b'])
L

# Change the element based on the index
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# Delete the element based on the index
print('Before change:', A)
del(A[0])
print('After change:', A)

# Split the string, default is by space
'hard rock'.split()

# Split the string by comma
'A,B,C,D'.split(',')

# Copy (copy by reference) the list A
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)
# Examine the copy by reference
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])
# Clone (clone by value) the list A
B = A[:]
B
# Now if you change A, B will not change:
print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])

######################### QUIZ: List #########################

a_list = [1,"hello",[1,2,3],True]
a_list

a_list[1]

a_list[1:4]

A = [1, 'a'] 
B = [2, 1, 'd']
A + B

## Scenario: Shopping list

### Task 1: Create an empty list
Shopping_list=[]

### Task 2: Now store the number of items to the shopping_list
    #### Watch
    #### Laptop
    #### Shoes
    #### Pen
    #### Clothes

Shopping_list=["Watch","Laptop","Shoes","Pen","Clothes"]

### Task 3: Add a new item to the shopping_list

Shopping_list.append("Football")
Shopping_list

### Task 4: Print First item from the shopping_list

print(Shopping_list[0])

### Task 5: Print Last item from the shopping_list

print(Shopping_list[-1])

### Task 6: Print the entire Shopping List

print(Shopping_list)

### Task 7: Print "Laptop" and "shoes"

print(Shopping_list[1:3])

### Task 8: Instead of "Pen" I want to buy "Notebook" let's change the item stored in the list.

Shopping_list[3] = "Notebook"

### Task 9: Let's delete items that are unimportant, such as; I don't want to buy Clothes, let's delete it.

del(Shopping_list[4])
Shopping_list

### Task 10: Print the shopping list

print(Shopping_list)

######################### END OF QUIZ #########################