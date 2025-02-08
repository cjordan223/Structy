# tree path finder

# Write a function, path_finder, that takes in the root of a binary tree and a target value. 
# The function should return an array representing a path to the target value.
# If the target value is not found in the tree, then return None.

# You may assume that the tree contains unique values.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def path_finder(root, target):
    if root.val == target:
        return [ root.val ]
    
    left_path = path_finder(root.left, target)
    if left_path is not None:
        return [rootval, *left_path]
        return [rootval, *right_path]
        
    right_path = path_finder(root.right, target)
    