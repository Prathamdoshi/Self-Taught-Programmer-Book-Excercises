# chapter 3 excecise solutions

# random library
import random 

# questions 1: Print three different strings 
print('\nQuestion 1 Solution: \n')

print("String #1")
print("String #2")
print("String #3")

print('*'*50)
# question 2: Write a program that prints if the number is less than 10 or greater than/equal to 10
print('\nQuestion 2 Solution: \n')

# random library used to generate random number between 1 and 15
x = random.randint(1,15)
print("Value for x: {}".format(x))

if x <10:
    print("Number is less than 10.")
elif x >= 10:
    print("Number is greater than or equal to 10.")

print('*'*50)

# question 3: Print something for number <=10, >10 or <=25, >25
print('\nQuestion 3 Solution: \n')

# random library used to generate random number between 1 and 15
x = random.randint(1,30)
print("Value for x: {}".format(x))

if x <=10:
    print("Number is less than 10.")
elif x > 10 and x<=25:
    print("Number is greater than 10 or less than/equal to 25.")
elif x > 25:
    print("Number is greater than 25.")

print('*'* 50)

# question 4: Create a program that divides two variable and prints the remainder 
print('\nQuestion 4 Solution: \n')

x = 15
y = 7
remainder = x % y
print("Values: x = {}, y = {}".format(x,y))
print("Remainder for x / y = {}".format(remainder))

print('*'* 50)

# question 5: Create a program that divides two variables, divides them and prints the quotient
print('\nQuestion 5 Solution: \n')

x = 15
y = 7
quotient = x // y
print("Values: x = {}, y = {}".format(x,y))
print("Quotient for x / y = {}".format(quotient))

print('*'* 50)

# question 6: Write a program that prints different strings for different range of ages. 
print('\nQuestion 6 Solution: \n')

# random library used to generate random number between 1 and 30
age = random.randint(1,30)  
print("Age: {}".format(age))

if age <=12:
    print("I hope those young, innocent and most fun days are going well.\n")
elif age > 12 and age<=19:
    print("Those teens can be tough! Hang in there pal.\n")
elif age >= 20 and age <= 29:
    print("The 20s are to explore to be young wild and free.\n")