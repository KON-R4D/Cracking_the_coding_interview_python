'''
QUESTION:
Validate BST: 
Implement a function to check if a binary tree is a binary search tree.

SOLUTION 1:

Our first thought might be to do an in-order traversal, copy the elements to an array,
and then check to see if the array is sorted. This solution takes up a bit of extra memory, 
but it works-mostly.
The only problem is that it can't handle duplicate values in the tree properly. 
However, if we assume that the tree cannot have duplicate values, then this approach works.
'''

# Helper Class
class Node():
    def __init__(self,item):
        self.left = None
        self.right = None
        self.data = item


######### our implementation 1 starts here ########### 

def validate_BTS(rootnode):
    resultant_array = validate_BTSHELPER(rootnode)
    return sorted(resultant_array.copy()) == resultant_array #check if array is sorted
    
    

def validate_BTSHELPER(rootnode): # helper function to return ordered array of nodes in the BST
    array=[]
    
    if rootnode is None:
        return array
    
    array.extend(validate_BTSHELPER(rootnode.left)+[rootnode.data]+validate_BTSHELPER(rootnode.right))
    return (array.copy())  # return left, current then right node


######### our implementation 1 ends here ########### 


'''
SOLUTION 2: (Modified version of that above)
We notice that we do not really need the entire array so just check the previous element to make sure it is
less than the current element
'''


######### our implementation 2 starts here ########### 

def validate_BTS_2(rootnode):
    prev_node = None
    
    if rootnode is None:
        return True
        
    if not validate_BTS(rootnode.left): # ensure the left side is valid. If not no need to proceed
        return False
        
    if prev_node !=None and rootnode.data <= prev_node: # ensure current node is less than or equal to previous
        return False
        
    prev_node = rootnode.data # set the new previous node
        
    if not validate_BTS(rootnode.right): # ensure that the right side is valid
        return False 
        
    return True

######### our implementation 2 ends here ########### 


'''
SOLUTION 3:
Keep track of the min and max value for each node and check for this
All children [nodes] to the left of parent node should be less than or equal to the node
All children [nodes] to the right of parent should be greater than the parent
'''


######### our implementation 3 starts here ########### 

def validate_BTS_3(rootnode):
    return validate_BTS_3HELPER(rootnode,None,None) #return return value of helper method

def validate_BTS_3HELPER(rootnode,min_,max_): 
    
    if rootnode is None:
        return True
    # if min value is set to a value, ensure current node is 
    if (min_ is not None and rootnode.data<= min_) or (max_ is not None and rootnode.data>max_):
        return False
    
    if (not validate_BTS_3HELPER(rootnode.left,None,rootnode.data)) or(not validate_BTS_3HELPER(rootnode.right,rootnode.data,None)):
        return False
    
    return True
######### our implementation 3 ends here ########### 



# Driver code

BTS_root = Node(20)
left = BTS_root.left = Node(10)
right = BTS_root.right = Node(30)
left.left = Node(5)
left.right = Node(15)


#validate_BTS(BTS_root)
#validate_BTS_2(BTS_root)
validate_BTS_3(BTS_root)