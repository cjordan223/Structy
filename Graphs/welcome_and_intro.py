#basic travesal algorithms

graph = {
"a": ["b", "c"],
"b":["d"],
"c": ["e"],
"d":["f"],
"e": [],
"f": []
}


#DFS

def depth_first_print(graph, start):
    
    stack = [start]
    while len(stack) > 0:
        current = stack[-1]
        print(current)
        stack.pop()   
        
        for neighbor in graph[current]:
            stack.append(neighbor)     

# RECURSIVE
def depth_first_print_r(graph, current):
    print(current)
    for neighbor in graph[current]:
        depth_first_print_r(graph, neighbor)

from collections import deque

def breadth_first_print(graph,start):

    queue = deque([ start ])
    while len(queue) > 0:
        current = queue[0]
        print(current)
        queue.popleft()  #FAST, runs in O(1)    
        for neighbor in graph[current]:
            queue.append(neighbor)
            
    
depth_first_print(graph, "a")
depth_first_print_r(graph, "a")
breadth_first_print(graph, 'a')
        
