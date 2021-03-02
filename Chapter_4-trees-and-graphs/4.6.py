'''
QUESTION:
Successor: 
Write an algorithm to find the "next" node (i.e., in-order successor) of a given 
node in a binary search tree. You may assume that each node has a link to its parent.


SOLUTION:
Recall that in-inorder traversal is in the form: left-node -> current node -> right-node
Based on this, if the current node has a right child, then the next node is the left most of that right node
Otherwise:
Get the top most parent in which the current node is it's left
'''

# Helper Class to hold node
class NodeWithParent():
    def __init__(self,node,parent):
        self.data = node
        self.left =None
        self.right = None
        self.parent = parent


######### our implementation starts here ########### 

def inOrder_successor(curr_node):
    if curr_node is None:
        return None
    
    def left_most_node(node): # function to get left most node
        if node is None:
            return None
        while node.left is not None: # go left while there is still a left child
            node = node.left
        return node
    
    if curr_node.right != None: # if there exists a right node,
        next_node = curr_node.right # get the left most of that right node
        return left_most_node(next_node) # since we would have already visited the left of current node
    
    else: # if no right node exists,
        curr = curr_node
        parent = curr.parent
        
        while (parent is not None) and (parent.left is not curr): # go up the chain to highest parent before
            curr = parent                                        # visiting the right hand side
            parent = curr.parent
        
        return parent
######### our implementation ends here ########### 


# Driver code

# Driver Code
BTS_root = NodeWithParent(1,None)

left = BTS_root.left = NodeWithParent(2, BTS_root)
right = BTS_root.right = NodeWithParent(3,BTS_root)

l_left = left.left = NodeWithParent(4,left)
r_left = left.right = NodeWithParent(5,left)

l_l_left =l_left.left=NodeWithParent(8,l_left)
r_l_left = l_left.right = NodeWithParent(9,l_left)
l_r_left = r_left.left = NodeWithParent(10,r_left)
r_r_left = r_left.right = NodeWithParent(11,r_left)

l_right = right.left = NodeWithParent(6,right)
r_right = right.right = NodeWithParent(7,right)


# expected order: 8->4->9->2->10->5->11->1->6->3->7


# inOrder_successor(r_l_left).data ==2 #9 -> 2
# inOrder_successor(l_r_left).data ==5 # 10->5
# inOrder_successor(left).data ==10 #2->10
inOrder_successor(l_left).data #4->9
