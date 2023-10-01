# Try Except Example
a = 1
try:
    b = int(input("Please enter a number to divide a: "))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")

# Try Except Specific Example
a = 1
try:
    b = int(input("Please enter a number to divide a: "))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")

# Try Except Else and Finally Example
a = 1
try:
    b = int(input("Please enter a number to divide a: "))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")


######################### PRACTICE: Exception Handling #########################

def safe_divide(numerator,denominator):
    try:
        result = (numerator/denominator)
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
numerator=int(input("Enter the numerator value: "))
denominator=int(input("Enter the denominator value: "))
print(safe_divide(numerator,denominator))

def Multi(no1,no2):
    try:
        multiplication=no1*no2
        print(multiplication)
    except ValueError:
        print('Invalid input! Please enter an integer or a float value.')
no1=float(input("Enter the first number: "))
no2=float(input("Enter the second number: "))
Multi(no1,no2)

def complex_calculation(num):
    try:
        result = num / (num - 5)
        print (f"Result: {result}")
    except Exception as e:
        print("An error occurred during calculation.")
# Test case
user_input = float(input("Enter a number: "))
complex_calculation(user_input)

######################### END OF PRACTICE #########################