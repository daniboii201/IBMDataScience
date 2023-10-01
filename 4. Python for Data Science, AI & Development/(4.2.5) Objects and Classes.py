# Import the library
import matplotlib.pyplot as plt

### Creating a Class

# Create a class Circle
class Circle(object):
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

### Creating an instance of a class Circle

# Create an object RedCircle
RedCircle = Circle(10, 'red')
# Find out the methods can be used on the object RedCircle
dir(RedCircle)
# Print the object attribute radius
RedCircle.radius
# Print the object attribute color
RedCircle.color
# Set the object attribute radius
RedCircle.radius = 1
RedCircle.radius
# Call the method drawCircle
RedCircle.drawCircle()

# Use method to change the object attribute radius
print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

# Create a blue circle with a given radius
BlueCircle = Circle(radius=100)
# Print the object attribute radius
BlueCircle.radius
# Print the object attribute color
BlueCircle.color
# Call the method drawCircle
BlueCircle.drawCircle()

### The Rectangle Class

# Create a new Rectangle class for creating a rectangle object
class Rectangle(object):
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
# Create a new object rectangle
SkinnyBlueRectangle = Rectangle(2, 3, 'blue')
# Print the object attribute height
SkinnyBlueRectangle.height
# Print the object attribute width
SkinnyBlueRectangle.width
# Print the object attribute color
SkinnyBlueRectangle.color
# Use the drawRectangle method to draw the shape
SkinnyBlueRectangle.drawRectangle()

# Create a new object rectangle
FatYellowRectangle = Rectangle(20, 5, 'yellow')
# Print the object attribute height
FatYellowRectangle.height 
# Print the object attribute width
FatYellowRectangle.width
# Print the object attribute color
FatYellowRectangle.color
# Use the drawRectangle method to draw the shape
FatYellowRectangle.drawRectangle()

######################### SCENARIO: Car dealership's inventory management system #########################

class Vehicle:
    color="white"
    # Constructor
    def __init__(self,max_speed,mileage):
        self.maxspeed = max_speed
        self.mileage = mileage
        self.capacity = None
    # Method
    def seating_capacity(self,capacity):
        self.capacity = capacity
    def printproperties(self):
        print("Properties of the vehicle: ")
        print("Color: ",self.color)
        print("Max speed: ",self.maxspeed)
        print("Mileage: ",self.mileage)
        print("Seating capacity: ",self.capacity)
# Creating objects of the Vehicle class
vehicle1 = Vehicle(200, 50000)
vehicle1.seating_capacity(5)
vehicle1.printproperties()

vehicle2 = Vehicle(180, 75000)
vehicle2.seating_capacity(4)
vehicle2.printproperties()

######################### END OF SCENARIO #########################