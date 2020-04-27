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

#hangman list
hangman_list = ["[1][3]",
                "[2][3]",
                "[3][2]",
                "[3][3]",
                "[3][4]",
                "[4][3]",
                "[5][2]",
                "[5][4]"]         

def hangman():
    for i in full_hangman:
        for j in i:
            print(j,end=' ')
        print(' ')

# data
#magic_word = w.generate_random_word()
magic_word = 'prathamd' #word to be guessed
magic_word_list = list(magic_word)

# status variables
number_of_chances = 8
user_response_list = []

print('Hangman: \n')
hangman()

game_start_string = "Press any key to start or 'q' to quit: "

while input(game_start_string) != 'q': 

   while number_of_chances > 0: 
    
    user_response = input("Guess the letter: ")

    if user_response in magic_word: 
        temp = magic_word.index(user_response)
        string = "{}{}= '{}'".format("full_hangman",hangman_list[temp],user_response)
        magic_word = magic_word.replace(user_response,'-',1)
        user_response_list.append(user_response)
        exec(string)
        hangman()
    
        if sorted(user_response_list) == sorted(magic_word_list):
            print('You won the game! Good job on guessing!!')
            game_start_string = "Press any key to restart the game or 'q' to quit: "
            break

    elif user_response not in magic_word:
        number_of_chances = number_of_chances - 1
        string = "{}{}= '{}'".format("full_hangman",hangman_list[number_of_chances]," ")
        exec(string)
        hangman()


    print("")

        

        
        


