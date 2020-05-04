# libraries 
import words as w

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

user_continue = True

while user_continue:

    key_word = w.generate_random_word()
    print("Key word: " + key_word + "\n")

    wrong_choice_number = 0
    guessed_word = []

    while wrong_choice_number < len(hangman):
       
    
    user_continue_response = input("Want to continue? 'y' for yes! 'n' for no: ")
    if user_continue_response == 'n':
        print("Thanks for Playing!")
        break;




