# level averages

# Write a function, level_averages, that takes in the root of a binary tree that contains number values. 
# The function should return a list containing the average value of each level.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from statistics import mean

def level_averages(root):
    levels = []
    fill_levels(root, levels, 0)
    avgs = []
    for level in levels:
        avgs.append(mean(level))
    return avgs
    
def fill_levels(root, levels, level_num):
    if root is None:
        return
    
    if len(levels) == level_num:
        levels.append([ root.val ])
    else:
        levels[level_num].append(root.val)
    
    fill_levels(root.left, levels, level_num + 1)
    fill_levels(root.right, levels, level_num + 1)