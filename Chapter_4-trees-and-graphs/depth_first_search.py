# with a depth first search, our aim is to visit deep before we visit wide.
# we will therefore follow a path till the end before we visit neighbouring paths
# picture it like following a road till its end before exploring any connected roads



def depth_first_search(starting_node):
    
    visited_nodes = set()
    
    def doSomething(item):
        # do something with the node
        # this could be printing it or any other thing to achieve the intended objective
        print(item)
    
    # from starting node, for each child follow each path till the end before visiting 
    # other children
    doSomething(starting_node)
    visited_nodes.add(starting_node)
    
    for node in adj[starting_node]:
        if node not in visited_nodes:
            depth_first_search(node)
        

# Driver Code 

# using adjacency list as implemented in file in this directory
depth_first_search(0) # 0->1->3->2