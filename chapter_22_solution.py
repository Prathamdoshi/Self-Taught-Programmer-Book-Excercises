# chapter 22 solution
# practicing all the algorithms 

# FizzBuzz challenge 
print('\nFizzbuzz Challenge: ')
for i in range(1,21):

    if i%3 == 0 and i%5 ==0:
        print("The number {} is divisible by 3 and 5".format(i))

    elif i%3 == 0:
        print("The number {} is divisible by 3".format(i))
    
    elif i%5 == 0:
        print('The number {} is divisible by 5'.format(i))
    else:
        print(i)
print('*'*50)
#--------------------------------------------------------------------------#

# sequetial search challenge 
print('\nSequential Search Challenge: ')

def sequential_search(number_list,n):
    if n in number_list:
        print("{} can be foud at index: {}".format(n,number_list.index(n)))
        return True
    elif n not in number_list:
        print("\n{} can't be found".format(n))
        return False


number_list = range(0,100)
print(sequential_search(number_list,5))
print(sequential_search(number_list,105))
print('*'*50)
#--------------------------------------------------------------------------#

# palindrome challenge
print('\nPalindrome Challenge: ')

def palindrome(word):
    return word.lower() == word[::-1].lower()

word = "Anna"
print("Word: {}".format(word))
print("Palindrome: {}\n".format(palindrome(word)))

word = "Pratham"
print("Word: {}".format(word))
print("Palindrome: {}\n".format(palindrome(word)))
print('*'*50)
#--------------------------------------------------------------------------#

# anagram challenge
print("\nAnagram Challenge: ")

def anagram(str_1,str_2):
    return sorted(str_1.lower()) == sorted(str_2.lower())

word_1 = 'cinema'
word_2 = 'iceman'

print("\nWord One: {}".format(word_1))
print("Word Two: {}".format(word_2))
print('Anagram: {}\n'.format(anagram(word_1,word_2)))

word_1 = 'pratham'
word_2 = 'doshi'

print("\nWord One: {}".format(word_1))
print("Word Two: {}".format(word_2))
print('Anagram: {}\n'.format(anagram(word_1,word_2)))
print('*'*50)
#--------------------------------------------------------------------------#

# Recurssion Challenge
print("\nRecurssion Challenge: ")

def bottles_of_beer(bob):
    if bob <1:
        print('No more bottles of beer on the wall. No more bottles of beer.')
        return 
    
    temp = bob
    bob = bob - 1
    print("{} bottles of beer on the wall. {} bottles of beer. Take down, pass it around, {} bottles of beer on the wall.".format(temp,temp,bob))
    bottles_of_beer(bob)

print("Output: \n")
bottles_of_beer(99)