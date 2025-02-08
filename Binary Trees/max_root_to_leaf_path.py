# max root to leaf path sum

# Write a function, max_path_sum, that takes in the root of a binary tree that contains number values. 
# The function should return the maximum sum of any root to leaf path within the tree.

# You may assume that the input tree is non-empty.

class Node {
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def max_path_sum(root):
    
    if root is None:
        return float('-inf')
    if root.left is None and root.right is None:
        return root.val
    max_left_sum = max_path_sum(root.left)    
    max_right_sum = max_path_sum(root.right)
    return root.val + max(max_left_sum, max_right_sum)    
    # if root is None:
    #     return float('-inf')
    # if root.left is None and root.right is None:
    #     return root.val
    # max_left_sum = max_path_sum(root.left)
    # max_right_sum = max_path_sum(root.right)
    # return root.val + max(max_left_sum, max_right_sum)
