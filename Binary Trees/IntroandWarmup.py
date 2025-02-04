#
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
a = None('a')
b = None('b')
c = None('c')
d = None('d')
e = None('e')
f = None('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right  = f

#       A
#      / \
#     B   C
#    / \  \
#   D  E   F 

# Write a function, depth_first_values, that takes in the root of a binary tree. 
# The function should return a list containing all values of the tree in depth-first order.

def depth_first_values(root):
     # need to return a list of all values in DFS order
     # stack solution:
     if root is None:
         return []
     
     stack = [root]
     while stack:
         current = stack.pop()
         print(current.val)
         
         if current.left is not None:
            stack.append(current.right)
         if current.right is not None:
            stack.append(current.left)