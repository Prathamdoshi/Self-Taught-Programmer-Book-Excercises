#library 
import os 
import random

# path to the file
cwd = os.getcwd()
filepath = os.path.join(cwd,"chapter_10_solution","data","words_raw.txt")

# container for the 8 letter words
words = []

# reading hadler 
with open(filepath, 'r', newline= '') as f:

    file_reader = f.read().split('\n')

    for line in file_reader:
        if len(line) > 3:
            words.append(line)
    
def generate_random_word():
    """
    Description: generates a random word from the list
    :return: Str
    """
    random_index = random.randint(1,len(words))
    return words[random_index]

if __name__ == '__main__':
    print("Words Module")
