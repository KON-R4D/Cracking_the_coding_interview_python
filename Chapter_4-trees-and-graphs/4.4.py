'''
QUESTION:

Check Balanced:

Implement a function to check if a binary tree is balanced. 
For the purposes of this question, a balanced tree is defined to be a tree such 
that the heights of the two subtrees of any node never differ by more than one.

SOLUTION:

For this we can do a recursive call and determine if at each node the right and left node do not differ by
more than one

'''

# Helper Class
class Node():
    def __init__(self,item):
        self.left = None
        self.right = None
        self.data = item


######### our implementation 1 starts here ########### 

def check_balanced(rootnode):
    if rootnode is None:
        return True
    
    diff = get_length(rootnode.right) - get_length(rootnode.left) # get the height difference between branches
    
    if abs(diff)>1: # if greater than 1 tree is unbalanced 
        return False
    return (check_balanced(rootnode.right) and check_balanced(rootnode.left))
    
    
def get_length(node):
    
    if node is None:
        return -1
    
    return max(get_length(node.left),get_length(node.right))+1 #recursive get length of longest branch


######### our implementation 1 ends here ########### 
    
    
'''
SOLUTION 2


'''

######### our implementation 2 starts here ########### 

def check_balanced_2(rootnode): 
    return (True if get_length_2(rootnode)!="ERROR_CODE" else False) #false if error code, true otherwise

        
def get_length_2(node):
    
    if node is None:
        return -1
    
    left_height = get_length_2(node.left) # get length of left node
    if left_height == "ERROR_CODE": # if error code, pass it on above
        return "ERROR_CODE"
    
    right_height = get_length_2(node.right) # get length of right node
    if right_height == "ERROR_CODE": # if error code, pass it on above
        return "ERROR_CODE"
    
    diff = left_height - right_height 
    
    if abs(diff)>1: # if unbalanced, pass on error code above
        return "ERROR_CODE"
    return (max(left_height,right_height)+1) # otherwise pass on actaul height calculated

######### our implementation 2 ends here ########### 


# Driver Code

rootNode = Node(1)
left = rootNode.left = Node(2)
right = rootNode.right = Node(3)
lleft = left.left = Node(4)
rleft = left.right = Node(5)
lright = right.left = Node(6)
rright = right.right = Node(7)

# tree above is balanced 
# uncomment code below to create unbalanced tree

#lrright = rright.left = Node(8)
#rrright = rright.right = Node(9)
#llrright = lrright.left = Node(10)

check_balanced_2(rootNode) #True

check_balanced(rootNode) #True
