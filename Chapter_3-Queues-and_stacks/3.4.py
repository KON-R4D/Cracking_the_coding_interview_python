'''
QUESTION:
Queue via Stacks:
Implement a MyQueue class which implements a queue using two stacks. 

SOLUTION:
Have an input and output stack. Push items into input stack. Then pop out of output stack.
If output stack is empty, pop then push everythig from input stack.
otherwise pop from output until it is empty

we make use of implementation of stack in the same directory
'''

######### our implementation starts here ###########

class MyQueue(MyStack):
    def __init__(self):
        self.in_stack = MyStack()
        self.out_stack = MyStack()
    
    def push(self, item):
        self.in_stack.push(item)
        
    def pop(self):
        val = self.out_stack.pop()
        if val:
            return val
        else:
            next_val = self.in_stack.pop()
            while next_val:
                self.out_stack.push(next_val)
                next_val = self.in_stack.pop()
            return self.out_stack.pop()
######### our implementation ends here ###########

# Driver code

q = MyQueue()
q.push(1)
q.push(2)
q.pop()
q.push(1)
q.push(3)
q.push(4)
q.pop()