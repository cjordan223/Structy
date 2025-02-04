# sum list

# Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument.
# The function should return the total sum of all values in the linked list.

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


def sum_list(head):
    if head is None:
        return 0
    return head.val + sum_list(head.next)

print(sum_list(a))