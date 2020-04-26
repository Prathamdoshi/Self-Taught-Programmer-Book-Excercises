# chapter 6 exercise solutions
#--------------------------------------------------------------------------#

# questions 1: Print every string in 'Camcus'
print('\nQuestion 1 Solution: \n')

string = 'Camcus'
print('Output: ')

for char in string:
    print(char)
print('*'*50)
#--------------------------------------------------------------------------#

# questions 2: Take two inputs and put them in a string
print('\nQuestion 2 Solution: \n')
# response_1 = input("What did you write yesterday? ")
# response_2 = input("Who did you send it to? ") 

print("Output: ")
print("Yesterday I wrote a {}. I sent it to {}.".format("response_1","response_2"))

print('*'*50)
#--------------------------------------------------------------------------#

# questions 3: Capitalize string "aldous Huxley was born in 1984."
print('\nQuestion 3 Solution: \n')
string = "aldous Huxley was born in 1984."

print("Original String: {}".format(string))
print("Capitalized String: {}".format(string.capitalize()))
print('*'*50)
#--------------------------------------------------------------------------#

# questions 4: Split "Where Now? Who Now? When Now?" into a list
print('\nQuestion 4 Solution: \n')
string = "Where now? Who now? When now? "

print("Output: ")
split_string = string.split("? ")

print(split_string)
print('*'*50)
#--------------------------------------------------------------------------#

# questions 5: list: ["The", "fox", "jumped", "over", "the", "fence","."]
print('\nQuestion 5 Solution: \n')
word_list = ["The", "fox", "jumped", "over", "the", "fence","."]
join_str = " ".join(word_list)
join_str = join_str[0:-2] + '.'
print(join_str)
print('*'*50)
#--------------------------------------------------------------------------#

# questions 6: String: "A screaming comes across the sky."
print('\nQuestion 6 Solution: \n')
string = "A screaming comes across the sky."

print("Original String: {}".format(string))
print("Replaced Char String: {}".format(string.replace('s','$')))
print('*'*50)
#--------------------------------------------------------------------------#

# questions 7: Use method to find index of the character'm in string 'Hemingway'
print('\nQuestion 7 Solution: \n')
string = 'Hemingway'
print('String: {}'.format(string))
print('Index for "m": {}'.format(string.index('m')))
print('*'*50)
#--------------------------------------------------------------------------#

# questions 8: Take three quotes and convert them to strings
print('\nQuestion 8 Solution: \n')
quote1 = "'Drink up,' said Ford, 'you've got three pints to get through.'"
quote2 = "'I forgot,' Lennie said softly. 'I tried not to forget. Honest to God I did, George.'"
quote3 = "'Yes,' I said, 'I have a reason,' and added very softly, 'My God.'"

print(quote1)
print(quote2)
print(quote3)
print('*'*50)
#--------------------------------------------------------------------------#

# questions 9: String "three three three" using concatenation and then again using multiplication
print('\nQuestion 9 Solution: \n')
string = "three "
print("String: {}".format(string))
print("String using concatenation: {}".format(string + string + string))
print("String using multiplication: {}".format(string*3))
print('*'*50)
#--------------------------------------------------------------------------#

# questions 10: take the string and slice it till coma
print('\nQuestion 10 Solution: \n')
string = "It was a bright cold day in April, and the clocks were striking thirteen."

index_number = string.index(',')
new_string = string[:index_number]

print("String: {}".format(string))
print("String till coma: {}".format(new_string))
print('*'*50)
#--------------------------------------------------------------------------#