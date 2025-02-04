#
# Primary goal of this dir is to get comfortbale with linked list traversal, both iteravitely and recursively. 
# Optinal complexity in O(n) time and O(1) space for iteration. O(n) & O(n) for recursive
# # 
# class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
        
        
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')


a.next = b
b.next = c
c.next = d


# A --> B --> C --> D --> None
# cur


def print_list(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next  
        
print_list(a)


def print_list_recurse(head):
    if head is None:
        return
    print(head.val)
    print_list_recurse(head.next)
    
print_list_recurse(a)

    
    