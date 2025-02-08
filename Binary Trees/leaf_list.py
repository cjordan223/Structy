# leaf list

# Write a function, leaf_list, 
# that takes in the root of a binary tree and returns a list containing the values of all leaf nodes in left-to-right order.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def leaf_list(root):
    if root is None:
        return []
    
    leaves = []
    
    stack = [root]
    while stack:
        current = stack.pop()
        
        if current.left is None and current.right is None:
            leaves.apppend(current.val)
        
        if current.right is not None:
            stack.append(current.right)
            
        if current.left is not None:
            stack.append(current.left)
            
            
    return leaves

