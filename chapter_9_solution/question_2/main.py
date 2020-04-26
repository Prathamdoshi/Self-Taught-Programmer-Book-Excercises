# chapter 9 exercise solutions
#--------------------------------------------------------------------------#

# questions 2: 
print('\nQuestion 2 Solution: \n')

# library
import os 

# path to the file
cwd = os.getcwd() 
file_path = os.path.join(cwd,"chapter_9_solution/question_2","output","output.txt")


# data 
questions = ["What is your name? ",'How old are you? ', "What is your favorite color? "] 
answers = []

print("Hello User! Please enter information: ")

#iterates through question bank to obtain answers
for question in questions:
    user_response = input(question)
    answers.append(user_response)

# using with, it opens the file and append all the question and answers to the output.txt file
with open(file_path,"w",newline='') as f:
    print('Writing to the file: ')
    f.write("Questions and Answers: \n")
    for i in range(len(questions)):
        f.write('Question: ' + questions[i] + '\n')
        f.write('Response: ' + answers[i] + '\n')
    print("Success! Please check the folder output under chapter_9_solution/question_2 folder.")  

