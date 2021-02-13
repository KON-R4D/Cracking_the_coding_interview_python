'''
QUESTION:
Delete Middle Node: Implement an algorithm to delete a node in the middle 
(i.e., any node but the first and last node, not necessarily the exact middle) 
of a singly linked list, given only access to that node.

SOLUTION:
since we do not have access to previous node, we will alter the data of the current node to that of the next
node then make current_node.next = next_node.next then delete next node

we will use a helper function to get reference to the middle node of interest

'''

# HELPER FUNCTION TO RETURN MIDDLE NODE #############
def return_Kth_node(LinkedList,K):
    next_node = LinkedList.head
    counter=1
    
    while next_node is not None:
        if counter==K:
            return next_node
        else:
            next_node = next_node.next
            counter+=1

# HELPER FUNCTION TO RETURN MIDDLE NODE #############


######### our implementation starts here ########### 

def delete_middle_node(middle_node):
    
    current_node = middle_node
    next_node = current_node.next
    current_node.data = next_node.data
    current_node.next = next_node.next
    next_node = None

######### our implementation ends here ########### 

# Driver Code

LL = LinkedList()
LL.append(1)
LL.append(2)
LL.append(3)
LL.append(4)
LL.append(5)

mid_node = return_Kth_node(LL,2)
delete_middle_node(mid_node)
LL.printList()