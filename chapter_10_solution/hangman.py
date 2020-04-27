# libraries 
import words as w

print('\n---------------HANGMAN---------------\n')
print('Welcome User! Here are the rules for the game: ')
print("""
      1. We have chose a random 8 letter word from dictionary. 
      2. You get 8 chances to guess the word. 
      3. Choosing the wrong letter will result in # of letters left deduction.
      4. To win the game, you have to guess the word in 8 tries or less. 
      5. To make this game more difficult, we have left the repeat letters on. A repeated letter has to be guessed twice.

      Good Luck! 
      """)

# entire hangman picture 
full_hangman = [["|","-","-","-","-"],
                ["|"," "," ","|"," "],
                ["|"," "," ","O"," "],
                ["|"," ","\\","|","/"],
                ["|"," "," ","|"," "],
                ["|"," ","/"," ","\\"]]            

def hangman():
    for i in full_hangman:
        for j in i:
            print(j,end=' ')
        print(' ')

print('Hangman: ')
hangman()

# data
#magic_word = w.generate_random_word()
magic_word = 'prathamd' #word to be guessed
