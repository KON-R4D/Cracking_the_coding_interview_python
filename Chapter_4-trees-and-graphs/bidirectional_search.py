# given two nodes in a graph with the intention of finding if there exists a path between the two
# we will perform two BFS instead of one keeping track of visited nodes and then returning
# true if we find any common child or the other node from the other

def biderectional_search(node1, node2):
    visited_nodes1 = set() # set to hold visited nodes from node1
    visited_nodes2 = set() # set to hold visited nodes from node2
    
    queue1 = [] # queue for first BFS
    queue2 = [] # queue for second BFS
    
    queue1.append(node1) # add node 1 to queue 1
    queue2.append(node2) # add node 2 to queue 2
    
    while queue1 or queue2:
        
        
        if queue1:
            top1 = queue1.pop(0)
            
        if queue2:
            top2 = queue2.pop(0)
        
        if top1 == node2 or top1 in visited_nodes2 or top2 == node1 or top2 in visited_nodes1:
            return True
        
        if top1 not in visited_nodes1:
            visited_nodes1.add(top1)
            for child1 in adj[top1]:
                queue1.append(child1)
                
        if top2 not in visited_nodes2:
            visited_nodes2.add(top2)
            for child2 in adj[top2]:
                queue2.append(child2)
                
        
    return False


# Driver code
# using adjacency list as implemented in file in this directory
biderectional_search(0,3) # True