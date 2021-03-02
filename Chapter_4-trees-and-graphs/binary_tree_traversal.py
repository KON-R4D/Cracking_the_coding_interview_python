'''
Here are the three common traversals 
'''

def inOrderTransversal(node):
    if node == None:
        return
    inOrderTransversal(node.left)
    visit(node)
    inOrderTransversal(node.right)
    
def preOrderTransversal(node):
    if node == None:
        return
    visit(node)
    preOrderTransversal(node.left)
    preOrderTransversal(node.right)
    
def postOrderTransversal(node):
    if node == None:
        return
    postOrderTransversal(node.left)
    postOrderTransversal(node.right)
    visit(node)


def visit(node):
    # A helper function to manipulate the node to achieve 
    # intended objective
