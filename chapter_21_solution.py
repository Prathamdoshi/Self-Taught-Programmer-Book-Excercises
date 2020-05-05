# chapter 21 solution

# practice: implement a stack class 
class Stack():

    def __init__(self):
        self.items = []
 

    def isEmpty(self):
        return self.items == []
    
    def push(self,value):
        self.items.append(value)
    
    def pop(self):
        value = self.items[-1]
        del self.items[-1]
        return value

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

# practice: implement a Queue class
class Queue():

    def __init__(self):
        self.items = []
    
    def enqueue(self,value):
        self.items.append(value)
    
    def dequeue(self):
        value = self.items[0]
        del self.items[0]
        return value
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

    def show(self):
        for i in self.items:
            print(i)


# question 1: reverse the string 'Yesterday' using a stack
print('\nQuestion 1 Solution: \n')
string = 'Yesterday'
reverse = ""
stack_1 = Stack() # instance

for char in string:
    stack_1.push(char)

for i in range(len(string)):
    reverse = reverse + stack_1.pop()

print("String: {}".format(string))
print("Reversed String: {}".format(reverse))
print('*'*50)
#--------------------------------------------------------------------------#

# question 2: create a new stack with the list reversed [1,2,3,4,5]
print('\nQuestion 2 Solution: \n')

a_list = [1,2,3,4,5]
n_list = []
stack_2 = Stack()

for i in range(len(a_list)):
    stack_2.push(a_list[i])
    
for i in range(len(a_list)):
    n_list.append(stack_2.pop())

print("Old List: {}".format(a_list))
print("Reversed List: {}".format(n_list))
print('*'*50)
#--------------------------------------------------------------------------#