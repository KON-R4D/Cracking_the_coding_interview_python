'''
QUESTION:
Implement a Queue with methods:

add(item): Add item to the end of the list
remove(): remove first item in list
peek(): Return the top of the queue
isEmpty(): return true iff the queue is empty

SOLUTION:
Use linked list to do this
'''

######### our implementation starts here ########### 

class Queue_LinkedList(Node):
    def __init__(self):
        self.head =None
        self.tail = None
    
    def add(self,item):
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def remove(self):
        if self.head.next is None:
            self.tail = None
        data = self.head.data
        self.head = self.head.next
        return data
        
    def peek(self):
        return self.head.data
    
    def isEmpty(self):
        return self.head is None and self.tail is None

######### our implementation ends here ########### 


# Driver code
q = Queue_LinkedList()
q.add(1)
q.peek()
q.add(2)
q.peek()
q.remove()
q.peek()
q.remove()
q.isEmpty()