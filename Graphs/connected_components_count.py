# connected components count

# Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. 
# The function should return the number of connected components within the graph.

def connected_components_count(graph):
    
    visited = set()
    
    count = 0
    
    for node in graph:
        
        if explore(graph, node, visited) == True:
            count += 1
    return count
        
def explore(graph, current, visited):
    
    if current in visited:
        
        return False
    
    visited.add(current)
    for neighbor in graph[current]:
        
        explore(graph, neighbor, visited)
    
    return True

print(connected_components_count({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})  ) #-> 1
