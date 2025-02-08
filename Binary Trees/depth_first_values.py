# depth first values

# Write a function, depth_first_values, that takes in the root of a binary tree. 
# The function should return a list containing all values of the tree in depth-first order.

# Hey. This is our first binary tree problem, so you should be liberal with watching the Approach and Walkthrough. 
# Be productive, not stubborn. -AZ

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):

  if root is None:
    return []
    
  stack = [root]
  values = []
  while stack:
    current = stack.pop()
    values.append(current.val)
    
    if current.right is not None:
      stack.append(current.right)
   
    if current.left is not None:
      stack.append(current.left)

  return values

 

  