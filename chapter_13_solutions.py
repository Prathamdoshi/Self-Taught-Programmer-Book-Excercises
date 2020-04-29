# chapter 13 exercise solutions
#--------------------------------------------------------------------------#

# questions 1: create a class called Rectangle and Square and add calculate perimeter to each.
print('\nQuestion 1 Solution: \n')

class Shape():
    def __init__(self):
        print("")

    def what_am_i(self):
        return("I am a shape.")

class Rectangle(Shape):

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def calculate_perimeter(self):
        return 2*(self.length+self.breadth)

class Square(Shape):

    def __init__(self,length):
        self.length = length 
    
    def calculate_perimeter(self):
        return 4*self.length
    
    # question 2 change_size implemented here:
    def change_size(self,amount):
        self.length = self.length + amount

rectangle_1 = Rectangle(10,20)
print("Rectangle One: ")
print("Length: {}".format(rectangle_1.length))
print("Breadth: {}".format(rectangle_1.breadth))
print("Perimeter: {}\n".format(rectangle_1.calculate_perimeter()))

square_1 = Square(10)
print("Square One: ")
print("Length: {}".format(square_1.length))
print("Perimeter: {}".format(square_1.calculate_perimeter()))
print('*'*50)
#--------------------------------------------------------------------------#

# questions 2: add a method in Square class that increaces and decreases size.
print('\nQuestion 2 Solution: \n')

# change_size() implemented above

# instances
square_1.change_size(10)
print("New Length(Increase): {}".format(square_1.length))
print("Perimeter: {}\n".format(square_1.calculate_perimeter()))

square_1.change_size(-15)
print("New Length(Decrease): {}".format(square_1.length))
print("Perimeter: {}".format(square_1.calculate_perimeter()))
print('*'*50)
#--------------------------------------------------------------------------#

# questions 3: Add a shape super class and make Square and Rectangle inherit from it
print('\nQuestion 3 Solution: \n')

# Class Square(), what_am_i implemented above

print("Superclass Inherited Test: ")
print("Square: {}".format(square_1.what_am_i()))

print("\nSuperclass Inherited Test: ")
print("Rectangle: {}".format(rectangle_1.what_am_i()))
print('*'*50)
#--------------------------------------------------------------------------#

# questions 4: Creat a Horse and Rider class and add composition connection between them
print('\nQuestion 4 Solution: \n')

class Horse():

    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Rider():
    def __init__(self,name):
        self.name = name

print("Testing Composition: \n")
print("Rider: ")
rider_1 = Rider("Pratham")
print("Rider Name: {}\n".format(rider_1.name))

print("Horse: ")
horse_1 = Horse("Sylvester Stallion","Pony",rider_1)
print("Horse name: {}".format(horse_1.name))
print("Horse breed: {}".format(horse_1.breed))
print("Horse Owner: {}".format(horse_1.owner.name))


print('*'*50)
#--------------------------------------------------------------------------#