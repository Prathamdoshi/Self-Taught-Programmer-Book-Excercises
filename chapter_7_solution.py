# chapter 7 exercise solutions
#--------------------------------------------------------------------------#

# questions 1: print each item in the list
print('\nQuestion 1 Solution: \n')
shows = ['The breaking bad','Game of thrones','Vampire Diaries','Money Heist']

print("Printing the Shows list: ")
for show in shows: print(show)
print('*'*50)
#--------------------------------------------------------------------------#
  
# questions 2: print numbers 25 to 50
print('\nQuestion 2 Solution: \n')
for i in range(25,51): print(i)
print('*'*50)
#--------------------------------------------------------------------------#

# questions 3: 
print('\nQuestion 3 Solution: \n')
for i in range(len(shows)):
    print("Index: {}, Show: {}".format(i,shows[i]))
print('*'*50)
#--------------------------------------------------------------------------#

# questions 4: 
print('\nQuestion 4 Solution: \n')

import random

while True: #infinite loop  
    x = random.randint(1,5) #use random library to get a number betwwen 1 and 5
    user_response = input('Guess a number(between 1 and 5) or enter "q" to quit: ')

    if user_response == "q":
        break
    try: 
        user_response = int(user_response)
    except:
        print('Please enter a number')
    if user_response == x:
        print("Correct Choice! The number was {}".format(x))
        break  
print('*'*50)
#--------------------------------------------------------------------------#

# questions 5: multiply two lists and append it a third list
print('\nQuestion 5 Solution: \n')
set_1 = [8,9,148,4]
set_2 =[9,1,33,83]
set_3 = []

for i in set_1:
    for j in set_2:
        k = i*j
        set_3.append(k)
print(set_3)

print('*'*50)
#--------------------------------------------------------------------------#
