# with a BFS, we visit neighbours before we visit children 
# for this we make use of a queue (FIFO)

def breadth_first_search(starting_node):
    
    def do_something_with_node(node): 
        # do something with the node here in line with intended goal of project
        print(node)
        
    visited_nodes = set()
    queue=[]
    
    queue.append(starting_node)
    
    
    while queue:
        top = queue.pop(0) # extract top of queue
        if top not in visited_nodes: # proceed if node wasn't previously visited already
            visited_nodes.add(top) # add node to visited nodes
            do_something_with_node(top) # manipulte information for intended purpose
            
            for child in adj[top]: # add node's children to the queue
                queue.append(child)


# Driver code 
# using adjacency list as implemented in file in this directory
breadth_first_search(0) #0->1->2->3