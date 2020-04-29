# chapter 11 exercise solutions
#--------------------------------------------------------------------------#

# questions 1: Defina a class called Apple with four instance variable that represent four attributes of an apple
print('\nQuestion 1 Solution: \n')
class Apple():
    def __init__(self,color, type_of_apple, weight, seadless):
        self.color = color
        self.type = type_of_apple
        self.weight = weight
        self.seadless = seadless

apple_1 = Apple("Dark Red", "Opal", 10.0, True)
print("Apple 1:")
print("Color: {}".format(apple_1.color))
print("Type: {}".format(apple_1.type))
print("Weight: {}".format(apple_1.weight))
print("Seadless: {}".format(apple_1.seadless))

print('*'*50)
#--------------------------------------------------------------------------#

# questions 2: Create a circle, with a method area
print('\nQuestion 2 Solution: \n')
import math

class Circle():

    def __init__(self, radius):
        self.radius = radius
    
    def change_radius(self, new_radius):
        self.radius = new_radius
    
    def area(self):
        return math.pi * self.radius * self.radius

circle_1 = Circle(radius=10)
print("Circle 1")
print("Radius: {}".format(circle_1.radius))
print("Area: {}\n".format(circle_1.area()))

circle_1.change_radius(20)
print("New Radius: {}".format(circle_1.radius))
print("New Area: {}".format(circle_1.area()))

print('*'*50)
#--------------------------------------------------------------------------#

# questions 3: 
print('\nQuestion 3 Solution: \n')
class Triangle():

    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def change_base_height(self,new_base,new_height):
        self.base = new_base
        self.base = new_height
    
    def area(self):
        return 0.5 * self.base * self.height

triangle_1 = Triangle(5,10)
print("Triangle 1")
print("Base: {}".format(triangle_1.base))
print("Height: {}".format(triangle_1.height))
print("Area: {}".format(triangle_1.area()))

triangle_1.change_base_height(15,20)
print("\nNew Base: {}".format(triangle_1.base))
print("New Height: {}".format(triangle_1.height))

print("New Area: {}".format(triangle_1.area()))
print('*'*50)
#--------------------------------------------------------------------------#

# questions 4: 
print('\nQuestion 4 Solution: \n')
class Hexagon():

    def __init__(self,length):
        self.length = length
    
    def change_length(self,new_length):
        self.length = new_length
    
    def calculate_perimeter(self):
        return 6 * self.length

hexagon_1 = Hexagon(length = 10)
print("Hexagon 1")
print("Side Lenght: {}".format(hexagon_1.length))
print("Perimeter: {}\n".format(hexagon_1.calculate_perimeter()))

hexagon_1.change_length(20)
print("New Side Lenght: {}".format(hexagon_1.length))
print("New Perimeter: {}\n".format(hexagon_1.calculate_perimeter()))

print('*'*50)
#--------------------------------------------------------------------------#