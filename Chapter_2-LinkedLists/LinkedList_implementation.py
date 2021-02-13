'''
Question:
Implementing a simple version of a linked list 
'''


######### our implementation starts here ###########
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class LinkedList(Node):
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif self.head.next is None:
            self.head.next = new_node
        else:
            next_node = self.head
            while next_node.next is not None:
                #print(next_node.data)
                next_node = next_node.next
            next_node.next = new_node
            
        self.size+=1
            
    
    def delete(self,node):
        #if head is node to be deleted
        if self.head.data == node:
            prev_head = self.head
            self.head = prev_head.next
            prev_head = None
            self.size-=1
        #otherwise find the node then delete
        else:
            runner1 = self.head
            runner2 = runner1.next
            
            while runner1.next is not None:
                if runner2.data == node:
                    runner1.next = runner2.next
                    runner2 = None
                    self.size-=1
                    return
                runner1,runner2 = runner1.next,runner2.next
        
    def findsize(self):
        counter=0
        next_node = self.head
        while next_node.next is not None:
            counter+=1
            next_node = next_node.next
        return counter+1
    
    def printList(self):
        next_node = self.head
        while next_node is not None:
            print(next_node.data,end=",")
            next_node = next_node.next
        
        
    
    
    def peek(self):
        return self.head
    
    def peekTail(self):
        next_node = self.head
        while next_node.next is not None:
            next_node = next_node.next
        return next_node


######### our implementation ends here ###########



# Driver code

LL = LinkedList()
LL.append(1)
LL.append(2)
LL.append(3)
LL.append(4)
LL.append(5)

LL.peek().data
LL.peekTail().data
LL.delete(4)
LL.printList()