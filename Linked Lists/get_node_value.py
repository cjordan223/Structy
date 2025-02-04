# get node value

# Write a function, get_node_value, that takes in the head of a linked list and an index. 
# The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

def get_node_value(head, index):
    while head is not None:
        head = head.next
        count += 1
        if count == index:
                return head.val 
        
    return None


def gnv_recurse(head, index):
    if head is None:
        return None
    if index == 0:
        return head.val
    
    gnv_recurse(head.next, index - 1)
