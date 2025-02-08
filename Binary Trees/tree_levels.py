# tree levels

# Write a function, tree_levels, that takes in the root of a binary tree. 
# The function should return a 2-Dimensional list where each sublist represents a level of the tree.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_levels(root):
    #DFS
    if root is None:
        return []
    
    levels = []
    stack = [(root, 0)]
    while stack:
        node, level_num = stack.pop()
        
        if len(levels) == level_num:
            levels.append([ node.val ])
            
                                     
        if node.right is not None:
            stack.append((node.right, level_num + 1))
            
        if node.left is not None:
            stack.append((node.left, level_num + 1))

                         
    return levels
        
        
        
  