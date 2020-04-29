# chapter 14 exercise solutions
#--------------------------------------------------------------------------#

# questions 1: create a square class just like the old chapters but this time add a squarelist variable
print('\nQuestion 1 Solution: \n')

class Square():
    square_list = []

    def __init__(self,length):
        self.length = length 
        self.square_list.append(self)
    
    def calculate_perimeter(self):
        return 4*self.length
    # modified by question 2 solution
    def __repr__(self):
        return "{} by {} by {} by {}.".format(self.length,self.length,self.length,self.length)

print("Squares Created:")
square_1 = Square(5)
square_2 = Square(5)
square_3 = Square(7)
square_4 = Square(8)

for i in range(len(square_1.square_list)):
    print("Square {}: {}".format(i ,square_1.square_list[i]))


print('*'*50)
#--------------------------------------------------------------------------#

# questions 2: implement a new __repr__ method
print('\nQuestion 2 Solution: \n')
# answer implemented above in the question 2 solution
print('*'*50)
#--------------------------------------------------------------------------#

# questions 3: create a function that compares two class intances and sees if they are the same.
print('\nQuestion 3 Solution: \n')

def variable_comparator(var_1, var_2):
    return var_1 is var_2

print("Check if two variables point to the same address: ")
print(variable_comparator(square_1,square_2))

print("\nSetting the variable to the same address and then calling the comparator: ")
square_2 = square_1
print(variable_comparator(square_1,square_2))

print('*'*50)
#--------------------------------------------------------------------------#