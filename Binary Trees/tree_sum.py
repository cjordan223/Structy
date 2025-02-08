# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None

# tree sum

# Write a function, tree_sum, that takes in the root of a binary tree that contains number values.
# The function should return the total sum of all values in the tree.

def tree_sum(root):
#   just compute the sum of the entire tree
    if root is None:
        return 0
    
    stack = [root]
    sum = 0

    while stack:
        current = stack.pop() 
        sum += current.val
        
        if current.right is not None:
            stack.append(current.right)
        
        if current.left is not None:
            stack.append(current.left)
        
    
    return sum
        
