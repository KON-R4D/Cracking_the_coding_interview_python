'''
QUESTION:
Partition: Write code to partition a linked list around a value x, 
such that all nodes less than x come before all nodes greater than or equal to x. 
If x is contained within the list, the values of x only need to be after the elements 
less than x (see below). The partition element x can appear anywhere in the "right partition";
it does not need to appear between the left and right partitions.


SOLUTION:
we create a new Linked List that will have a pivot value of x, all values less than x will be added as head
while all values greater than or equal to x will be added as tail of the new linked list
we will then return the new head of the list
'''


######### our implementation starts here ########### 

def partition_linked_list_aroud_pivot(LinkedList,x):
    next_node = LinkedList.head
    head = next_node
    tail = next_node
    
    while next_node is not None:
        next_= next_node.next
        if next_node.data >=x:
            #place on the right (from tail)
            tail.next = next_node
            tail = next_node
        else:
            #place on the left (from head)
            next_node.next = head
            head = next_node
            
        
        next_node = next_
        
    tail.next = None 
    return head


######### our implementation ends here ########### 


# Driver code

LL = LinkedList()
LL.append(3)
LL.append(2)
LL.append(4)
LL.append(6)
LL.append(5)
LL.append(13)
LL.append(1)

new_head = partition_linked_list_aroud_pivot(LL,4)
LL.head = new_head
LL.printList()