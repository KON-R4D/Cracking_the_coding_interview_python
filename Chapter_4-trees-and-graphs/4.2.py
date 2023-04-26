'''
QUESTION: 
Minimal Tree:
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.


SOLUTION:
To create a tree of minimal height, we need to match the number of nodes in 
the left subtree to the number of nodes in the right subtree as much as possible. 
This means that we want the root to be the middle of the array, since this would 
mean that half the elements would be less than the root and half would be greater than it.
'''


######### our implementation starts here ###########

# we will start by creating our representation of a node
# will have left and right values in addition to data values

class Node:
    #constructor
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
    
    #add left node
    def addleft(self,node):
        self.left = Node(node)
        
    #add right node   
    def addright(self,node):
        self.right = Node(node)
        
#function to take array and split it up into variables for helper method
def createMIN_BST(array):
    return createMIN_BST_Helper(array,0,len(array)-1)

#helper method that recursively inserts the midpoint to create the MIN_BST
def createMIN_BST_Helper(array,start,end):
    if end<start:
        return
    midpoint = (start+end)//2
    
    node =Node(array[midpoint])
    node.left = createMIN_BST_Helper(array,start,midpoint-1)
    node.right = createMIN_BST_Helper(array,midpoint+1,end)
    return node
    
        
    #print(len(array)//2)

    #node = Node(3)
    #node.addleft(4)
    #array= [1,2,3,4,5]
    #midpoint = len(array)//2
        
######### our implementation ends here ###########


#Driver Code
array = [10,12,3,4,54,6,56,43,23,14,2,18,68]
array = sorted(array)

#create the binary search tree
#createBST(array)

MIN_bst = createMIN_BST(array)
#print(array)
#print(bst.left.right.right.data)=12
