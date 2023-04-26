'''
QUESTION:
Implement a stack with methods:

pop(): Remove top item from stack
push(): Add item to top of stack
peek(): Return the top of the stack
isEmpty(): return true iff the stack is empty

SOLUTION:
Use linked list to do this
'''

######### our implementation starts here ########### 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class MyStack_LinkedList(Node):
    
    def __init__(self):
        self.head =None
        
    def push(self,item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        top = self.head.data
        next_node = self.head.next
        self.head = None
        self.head = next_node
        return top
    
    def peek(self):
        if self.head is None:
            return
        return self.head.data
    
    def isEmpty(self):
        return self.head == None

######### our implementation ends here ###########


# Driver code

stacker = MyStack_LinkedList()
stacker.push(1)
stacker.push(2)
stacker.push(3)
stacker.peek()
stacker.pop()
stacker.peek()
