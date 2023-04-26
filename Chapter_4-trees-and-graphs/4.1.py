'''
QUESTION: 
Route Between Nodes:
Given a directed graph, design an algorithm to find out whether there is a route between two nodes


SOLUTION:
Utilize a BFS starting from one node to determine if we will reach a given node
'''

### ********** ####

# To solve this, we would need to be handed a graph so this is a simple helper function to create the graph
# We may not have to implement it if given the actual graph
# Here I use an adjacency list to represent the graph in the Graph Class

from collections import defaultdict

class Graph:
    
    #constructor
    def __init__(self):
        self.graph = defaultdict(list)
        
    #add edges to graph
    def addEdge(self, u,v):
        self.graph[u].append(v)
    
    #return graph
    def view(self):
        return self.graph

### ********** ####


######### our implementation starts here ###########


def search(graph_,start_node,end_node):
    
    #if the start and end are the same, then there is a path
    if start_node ==end_node:
        return True
    
    graph = graph_.view()
    
    #perform BFS on graph
    
    visited =[False]*(max(graph)+1) #array to handle visited nodes 
    
    queue = [] #queue to handle our order of transversal
    
    #add start node into queue
    queue.append(start_node)
    
    #while queue is not empty
    while queue:
        
        #pop out item at beginning of queue
        curr_node = queue.pop(0)
        
        #mark it as visited
        visited[curr_node]=True
        
        #extract any adjacent nodes to current node and add them to the queue
        for adj_node in graph[curr_node]:
            #if adjacent node is not already visited...
            if not visited[adj_node]==True:
                # if it is the same as the end node..
                if adj_node == end_node:
                    #then a path does exist and we are done doing the search
                    return True
                
                #otherwise add it to the queue
                queue.append(adj_node)
                
        
    return False
            

######### our implementation ends here ############


# Driver code

# Create a graph using the class Graph above
g = Graph()

# add edges to graph
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


# check if a route exists
search(g,2,3)
