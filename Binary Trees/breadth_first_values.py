# breadth first values

# Write a function, breadth_first_values, that takes in the root of a binary tree. 
# The function should return a list containing all values of the tree in breadth-first order.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def breadth_first_values(root):
    
    # recall needing a STACK to work with the DFS list
    # a QUEUE is needed for BFS
    if root is None:
        return []
    
    queue = [root]
    values = []
    
    while queue:
        current = queue.pop(0)
        values.append(current.val)
        
        if current.left:
            queue.appened(current.left)
        
        if current.right:
            queue.appened(current.right)
      
    return values
        
