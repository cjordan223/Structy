# minimum island

# Write a function, minimum_island, that takes in a grid containing Ws and Ls. 
# W represents water and L represents land. The function should return the size of the smallest island. 
# An island is a vertically or horizontally connected region of land.

# You may assume that the grid contains at least one island.

# instead of doing an island count like the last problem, you are just returning the size of the smallest island
# per


def minimum_island(grid):
  visited = set()
  
  min_size = float('inf')
  
  for c in range(len(grid)):
    for r in range(len(grid[0])):
        explore_size(grid, r, c, visited) #TODO
        if size < min_size:
            min_size = size
    return min_size
  
  
  return min_size


def explore_size(grid, r, c, visited):
    
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])
    
    if not row_inbounds or not col_inbounds:
        return 0
    
    if grid[r][c] == 'W':
        return 0
    
    pos = (r, c)
    
    if pos in visited:
        return 0
    
    visited.add(pos)
    
    size = 1
    
    size += explore_size(grid, r+1, c, visited)
    size += explore_size(grid, r-1, c, visited)
    size += explore_size(grid, r, c+1, visited)
    size += explore_size(grid, r, c-1, visited)
    
    return size