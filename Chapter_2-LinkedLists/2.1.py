'''
QUESTION:
Write code to remove duplicates from an unsorted linked list.

SOLUTION:
Will be O(n) since it is unsorted so we will have to transverse through the entire linked list.
Utilize a hashmap to store existing values and if they exist, skip them

we make use of the linked list implementation found in this very directory
'''

######### our implementation starts here ###########

from collections import defaultdict
def removeDuplicateNodes(LinkedList):
    dictionary=defaultdict()
    prev_node = LinkedList.head
    curr_node = prev_node.next
    
    dictionary[prev_node.data]=True
    
    while curr_node is not None:
        #print(curr_node.data)
        if dictionary.get(curr_node.data,False):
            prev_node.next = curr_node.next
        else:
            prev_node.next = curr_node
            dictionary[curr_node.data]=True
            prev_node = curr_node
        curr_node = curr_node.next
    #print(dictionary)
            
            
######### our implementation ends here ########### 


######### our implementation 2 starts here ###########     
   
def deleteDuplicateNodes(LinkedList):
    holding_set = set()
    prev_node = None
    curr_node = LinkedList.head
    
    while curr_node is not None:
        #print(curr_node.data)
        if curr_node.data in holding_set:
            prev_node.next = curr_node.next
        else:
            holding_set.add(curr_node.data)
            prev_node = curr_node
        curr_node = curr_node.next
    #print(dictionary)

 ######### our implementation 2 ends here ###########        
        


# Driver code

LL = LinkedList()
LL.append(1)
LL.append(2)
LL.append(3)
LL.append(4)
LL.append(3)
LL.append(1)
LL.append(6)
LL.append(6)

removeDuplicateNodes(LL)
#deleteDuplicateNodes(LL)

        
        