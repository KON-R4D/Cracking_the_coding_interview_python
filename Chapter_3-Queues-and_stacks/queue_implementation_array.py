'''
QUESTION:
Implement a Queue with methods:

add(item): Add item to the end of the list
remove(): remove first item in list
peek(): Return the top of the queue
isEmpty(): return true iff the queue is empty

SOLUTION:
Use an array to do this
'''

######### our implementation starts here ########### 

class Queue():
    
    def __init__(self):
        self.queue=[]
        
    def add(self,item):
        self.queue.append(item)
    
    def remove(self):
        #return self.queue.pop(0)
        top = self.queue[0]
        del self.queue[0]
        return top
    
    def peek(self):
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queque)==0

######### our implementation ends here ########### 

# Driver code
q = Queue()
q.add(1)
q.add(2)
q.peek()
q.add(3)
q.remove()
