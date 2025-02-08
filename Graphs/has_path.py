# has path
# Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph 
# and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path 
# between the source and destination nodes.


graph = { 
"f": ["g","i"],
"g": ["h"],
"h": [],
"i": ["g","k"],
"j": ["i"],
"k": [] 
}


#complexity? # edges (e), # nodes (n)
# Time: O(e)
# Space: O(n)
# Can also just be represented by:  
    # n = nodes, n^2 is edges
    # Time: O(n^2)
    # Space: O(n)


def has_path(graph, src, dst):
    if src == dst:
        return True
    
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst) == True:
            return True
    
    return False
