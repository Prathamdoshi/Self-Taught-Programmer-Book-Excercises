# chapter 9 exercise solutions
#--------------------------------------------------------------------------#

# questions 1: 
print('\nQuestion 1 Solution: \n')

# library
import os 

# path to the file
cwd = os.getcwd() 
file_path = os.path.join(cwd,"chapter_9_solution/question_1","data","test.txt")
# using with to read in the contents of the file
with open(file_path,'r') as f:
    print("Read the input from the file and print it below: ")
    print(f.read())

print('*'*50)
#--------------------------------------------------------------------------#

