# largest component

# Write a function, largest_component, that takes in the adjacency list of an undirected graph. 
# The function should return the size of the largest connected component in the graph.

def largest_component(graph):

  
  visited = set()
  largest = 0
  
  for node in graph:
      size = explore_size(graph, node, visited)
      if size > largest:
        largest = size

  return largest

def explore_size(graph, node, visited):
  if node in visited:
    return 0

  visited.add(node)

  size = 1
  for neighbor in graph[node]:
    size += explore_size(graph, neighbor, visited)

  return size

largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4


  