# linked list find

# Write a function, linked_list_find, that takes in the head of a linked list and a target value. 
# The function should return a boolean indicating whether or not the linked list contains the target.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
        
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

def linked_list_find(head, target):
    while head is not None:
        if head.val == target:
            return True
        head = head.next
        
    return False


print(linked_list_find(a,3))
print(linked_list_find(a,4))        
        