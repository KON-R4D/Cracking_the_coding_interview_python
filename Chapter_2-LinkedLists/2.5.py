'''
QUESTION:
Sum Lists: You have two numbers represented by a linked list, 
where each node contains a single digit.The digits are stored in reverse order, 
such that the 1 's digit is at the head of the list. 
Write a function that adds the two numbers and returns the sum as a linked list.

SOLUTION: O(m+n)
we will read out the values into a stack (FILO) as we traverse through the linkedlist then once done 
pop out values from the two stacks, convert them into an int then sum them up
'''


######### our implementation starts here ########### 

def sum_lists_backwards(linkedlist1, linkedlist2):
    stack1 = []
    stack2 = []
    
    string1=""
    string2=""
    
    #first iterate through the different lists
    
    next_node = linkedlist1.head# process linkedlist1
    
    while next_node is not None:
        stack1.append(next_node.data)
        next_node = next_node.next
        
    next_node = linkedlist2.head # process linkedlist2
    
    while next_node is not None:
        stack2.append(next_node.data)
        next_node = next_node.next
        
    while stack1:
        string1 = str(stack1.pop(0))+string1 # string1+stack1.pop(-1)
    while stack2:
        string2 = str(stack2.pop(0))+string2
    
    return int(string1)+int(string2)

######### our implementation ends here ########### 
        
'''
FOLLOW UP:
Suppose the digits are stored in forward order. Repeat the above problem.

SOLUTION:
We will use a queue instead of a stack to do this
'''


######### our implementation starts here ########### 

def sum_lists_forwards(linkedlist1, linkedlist2):
    queue1 = []
    queue2 = []
    
    string1=""
    string2=""
    
    #first iterate through the different lists
    
    next_node = linkedlist1.head# process linkedlist1
    
    while next_node is not None:
        queue1.append(next_node.data)
        next_node = next_node.next
        
    next_node = linkedlist2.head # process linkedlist2
    
    while next_node is not None:
        queue2.append(next_node.data)
        next_node = next_node.next
        
    while queue1:
        string1 = string1+ str(queue1.pop(0)) # string1+stack1.pop(-1)
    while queue2:
        string2 = string2+str(queue2.pop(0))
    
    return int(string1)+int(string2)

    ######### our implementation ends here ########### 


# Driver code 

LL1 = LinkedList()
LL1.append(7)
LL1.append(1)
LL1.append(6)


LL2 = LinkedList()
LL2.append(5)
LL2.append(9)
LL2.append(2)

sum_lists_backwards(LL1,LL2)

sum_lists_forwards(LL1,LL2)