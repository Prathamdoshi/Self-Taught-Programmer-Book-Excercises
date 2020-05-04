# libraries 
import words as w
import collections

print('\n---------------HANGMAN---------------\n')
print('Welcome User! Here are the rules for the game: ')
print("""
      1. We have chosen a random word from dictionary. 
      2. You get 6 chances to guess the word. 
      3. Choosing the wrong letter will result in # of letters left deduction.
      4. To win the game, you have to guess the word in 6 tries or less. 
      5. To make this game more difficult, we have left the repeat letters on. A repeated letter has to be guessed twice.

      Good Luck! 
      """)

hangman = [
          "________      ",
          "|      |      ",
          "|      |      ",
          "|      0      ",
          "|     /|\     ", 
          "|     / \     ",
          ]

# variable to hold user's response to continue the game
user_continue = True

while user_continue:

    key_word = w.generate_random_word() # use the module to get a word
    key_word_list = list(key_word) # convert it to list to map it with the guessed word
    wrong_choice_number = 0 # tracks the number of wrong responses 
    guessed_word = [] # holds all the correct letters in a string
    dash_str = len(key_word)*['_',] # dash representation of the word
  

    while wrong_choice_number < len(hangman): 
        print("\nWord: ")
        for dash in dash_str: print(dash,end=" ") # prints the dashes for the word
        print("\n")
        guessed_letter = input("Guess the letter: ")

        if guessed_letter in key_word:
            temp = key_word_list.index(guessed_letter) # get the index of the letter
            dash_str[temp] = guessed_letter # change the dash with the right letter
            key_word_list[temp]='_' # devalue the old letter so it handles repeats correctly
            guessed_word.append(guessed_letter) # collect it for a further match
        
        if guessed_letter not in key_word:
           for i in range(0,wrong_choice_number+1): # prints the hangman till the stage user has corrected wrong
               print(hangman[i])
           wrong_choice_number = wrong_choice_number + 1 # increaces the penalty

        if collections.Counter(sorted(guessed_word)) == collections.Counter(sorted(list(key_word))): # word match check
            print ("\nCongratulations!! You guessed the word '{}' correctly.\n".format(key_word)) # win handler
            break;
        
    if wrong_choice_number >=6: # lost check
        print('\nSorry you loss.') # losing handler
        
    
    user_continue_response = input("Want to continue? 'y' for yes! 'n' for no: ") # user continue check
    if user_continue_response == 'n':
        print("\nThanks for Playing!\n")
        break;




