'''
QUESTION:
Stack Min: 
How would you design a stack which, in addition to push and pop, has a function min which 
returns the minimum element? Push, pop and min should all operate in 0(1) time.


pop(): Remove top item from stack
push(): Add item to top of stack
peek(): Return the top of the stack
isEmpty(): return true iff the stack is empty

SOLUTION:
have an array that will store the min value for each addition. delete min with each pop
'''


######### our implementation starts here ###########

class Stack_withMin(Node):
    def __init__(self):
        self.stack= []
        self.min_at_each_step = [] # array to capture minimum valuea at each state
        self.min = 0
        
    def push(self,item):
        
        if self.isEmpty():
            self.min_at_each_step.append(item)
            self.min = item
        else:
            self.min = min(self.min,item)
            self.min_at_each_step.append(self.min)
        self.stack.append(item)
            
        
        
    def pop(self):
        if self.isEmpty():
            return
        data = self.stack[-1]
        del self.stack[-1]
        del self.min_at_each_step[-1]
        return data
    
    def peek(self):
        if self.isEmpty():
            return
        return self.stack[-1]
    
    def peek_min(self):
        if self.isEmpty():
            return
        return self.min_at_each_step[-1] #pop last is O(1) in python: https://wiki.python.org/moin/TimeComplexity
    
    def isEmpty(self):
        return len(self.stack)==0
    
    
######### our implementation ends here ###########



# Driver code

s = Stack_withMin()
s.push(5)
s.push(4)
s.push(3)
s.push(5)
s.push(2)
s.push(1)

s.peek_min()
s.pop()
s.pop()
s.peek_min()