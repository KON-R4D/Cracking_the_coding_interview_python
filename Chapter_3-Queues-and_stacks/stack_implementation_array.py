'''
QUESTION:
Implement a stack with methods:

pop(): Remove top item from stack
push(): Add item to top of stack
peek(): Return the top of the stack
isEmpty(): return true iff the stack is empty

SOLUTION:
Use an array to do this
'''

######### our implementation starts here ########### 

class MyStack():
    def __init__(self):
        self.stack =[]
    
    def pop(self):
        if len(self.stack)==0:
            return False
        
        value = self.stack[-1]
        del self.stack[-1]
        return value
    
    def push(self, item):
        self.stack.append(item)
    
    def peek(self):
        if len(self.stack)==0:
            return False
        return self.stack[-1]
    
    def isEmpty():
        return len(self.stack)==0

######### our implementation ends here ########### 


# Driver code
stack = MyStack()
stack.push(1)
stack.peek()
stack.push(2)
stack.peek()
stack.pop()
        
    