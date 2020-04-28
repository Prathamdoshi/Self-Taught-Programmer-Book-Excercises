# # libraries 
# import words as w

# print('\n---------------HANGMAN---------------\n')
# print('Welcome User! Here are the rules for the game: ')
# print("""
#       1. We have chose a random 8 letter word from dictionary. 
#       2. You get 8 chances to guess the word. 
#       3. Choosing the wrong letter will result in # of letters left deduction.
#       4. To win the game, you have to guess the word in 8 tries or less. 
#       5. To make this game more difficult, we have left the repeat letters on. A repeated letter has to be guessed twice.

#       Good Luck! 
#       """)

# stages = [
#           "________      ",
#           "|      |      ",
#           "|      0      ",
#           "|     /|\     ", 
#           "|     / \     ",
#           "|"]

        

import random


def hangman():
    word_list = ["Python", "Java", "computer", "hacker", "painter"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print('Welcome to Hangman')
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Guess a letter")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in letter_board:
            print('You win! The word was:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The words was {}'.format(word))

hangman()


