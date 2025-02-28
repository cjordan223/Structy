# reverse list

# Write a function, reverse_list, that takes in the head of a linked list as an argument. 
# The function should reverse the order of the nodes in the linked list in-place and return 
# the new head of the reversed linked list.

#
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

def reverse_list(head):
    current = head
    previous = None
    
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
        
    return previous
   
print(reverse_list("a")) 
    

