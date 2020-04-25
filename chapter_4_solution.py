# chapter 4 exercise solutions
#--------------------------------------------------------------------------#
# random library
import random 

# questions 1: Write a function that takes a number as an input and returns the number squared.
print('\nQuestion 1 Solution: \n')

# random library used to generate random number between 1 and 5
x = random.randint(1,5)
print("Value for x: {}".format(x))

def square_handler(x):
    """
    Description: function handler for squaring
    :param x: Int
    :return: Int
    """
    print ("Squared Result: {}".format(x**2))

# function call
square_handler(x)
print('*'*50)
#--------------------------------------------------------------------------#

# questions 2: Write a function that accepts a string as a parameter and prints it.
print('\nQuestion 2 Solution: \n')

def str_handler(x:str):
    """
    Description: print handler for a string
    :param x: Str
    """
    print(x)

# function call
str_handler("Pratham")
print('*'*50)
#--------------------------------------------------------------------------#

# questions 3: Write a function that accepts three required params and two optional params. 
print('\nQuestion 3 Solution: \n')

def add(x,y,z,a=0,b=0):
    """
    Description: adds all the parametres
    :param x: Int,
    :param y: Int
    :param z: Int
    :param a(optional): Int
    :param b(optional: Int
    :return: Int
    """
    print("Values: x:{}, y:{}, z:{}, a:{}, b:{}".format(x,y,z,a,b))
    return x + y + z + a + b

# function call
print("Total: {}".format(add(1,2,3)))
print('*'*50)
#--------------------------------------------------------------------------#

# questions 4: Two functions: 1) Int as param and return divided it by two. 2) Take return from 1 and return * 4.
print('\nQuestion 4 Solution: \n')

# random library used to generate random number between 1 and 10
x = random.randint(1,10)
print("Value for x: {}".format(x))

def divide_by_two(x):
    """
    Description: divides the parameter by half
    :param x: Int
    :return: Int
    """
    return x/2

def multiply_by_four(x):
    """
    Description: multiplies the parameter by 4
    :param x: Int
    :return: Int
    """
    return x*4

# function call
print("x divided by 2: {}".format(divide_by_two(x)))
print("x/2 multiplied by 4: {}".format(multiply_by_four(divide_by_two(x))))
print('*'*50)
#--------------------------------------------------------------------------#

# questions 5: Write a function that converts a string to float and add error handler. 
print('\nQuestion 5 Solution: \n')

str_1 = "3.0"
str_2 =  "Error Generator"

def str_to_float(x:str):
    """
    Description: str to float handler with an error handler
    :param x: str
    :return: float
    """
    y = float()
    try:
       y = float(x)
    except ValueError:
        print("Can't convert to Float\n")
        return None
    print("Success! Float: {}, Type: {}\n".format(y,type(y)))
    return y

# function call
print("String 1: {}".format(str_1))
str_to_float(str_1)
print("String 2: '{}'".format(str_2))
str_to_float(str_2)

print('*'*50)
#--------------------------------------------------------------------------#