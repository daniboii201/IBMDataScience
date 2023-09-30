# For loop example
dates = [1982,1980,1973]
N = len(dates)
for i in range(N):
    print(dates[i])
# Example of for loop
for i in range(0, 8):
    print(i)
# Exmaple of for loop, loop through list
for year in dates:  
    print(year)  

# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

# Loop through the list and iterate on both index and element value
squares=['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)

count = 1
while count <= 5:
    print(count)
    count += 1

# While Loop Example
dates = [1982, 1980, 1973, 2000]
i = 0
year = dates[0]
while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
print("It took ", i ,"repetitions to get out of loop.")

######################### QUIZ: Loops #########################

for i in range(-5, 6):
    print(i)

Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)

squares=['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print (square)

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0
rating = PlayListRatings[0]
while(i<len(PlayListRatings) and rating>=6):
    print(rating)
    i=i+1
    rating = PlayListRatings[i]

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i=0
while(i<len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i=i+1
print(new_squares)

print("Multiplication table of 6:")
for six in range(11):
    print("6 *",six,"=",6*six)
print("Multiplication table of 7:")
for seven in range(11):
    print("7 *",seven,"=",7*seven)

Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
essay_Animals = []
i=0
while(i<len(Animals)):
    if(len(Animals[i]) == 7):
        essay_Animals.append(Animals[i])
    i=i+1
print(essay_Animals)

######################### END OF QUIZ #########################