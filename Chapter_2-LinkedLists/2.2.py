'''
QUESTION:
Return Kth to Last: 
Implement an algorithm to find the kth to last element of a singly linked list.

SOLUTION:
Have 2 pointers that will first extend the length of K between them then iterate 
as usual till the end and return the Kth element

we make use of the linked list implementation found in this very directory
'''
######### our implementation starts here ########### 

def return_Kth_to_last_element(LinkedList,K):
    runner1 = LinkedList.head
    runner2 = runner1.next
    counter=0
    
    while runner2 is not None:
        if counter<K:
            runner2 = runner2.next
            counter+=1
        else:
            runner2=runner2.next
            runner1= runner1.next
            counter+=1
            
    return runner1.data

######### our implementation ends here ########### 

# Driver Code

LL = LinkedList()
LL.append(1)
LL.append(2)
LL.append(3)
LL.append(4)
LL.append(5)

return_Kth_to_last_element(LL,3)