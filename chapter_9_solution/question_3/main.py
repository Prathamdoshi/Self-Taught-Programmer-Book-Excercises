# chapter 9 exercise solutions
#--------------------------------------------------------------------------#

# questions 3: 
print('\nQuestion 2 Solution: \n')

# libraries
import os
import csv 

# path to the file
cwd = os.getcwd() 
file_path = os.path.join(cwd,"chapter_9_solution/question_3","output","output.csv")

data = [["Titanic","The Revenant","Inception"],
        ['Top Gun','Risky Business','Minority Report'],
        ['Breaking Bad','Money Heist','Too Hot to Hanlde']]

print('---Writing to the file:---')
with open(file_path,'w') as f:
    
    csvwriter = csv.writer(f,
                           delimiter = ",")
    for row in data:
        csvwriter.writerow(row)
      
print("Success! Please check the folder output under chapter_9_solution/question_3 folder.")  