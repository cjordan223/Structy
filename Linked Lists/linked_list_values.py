# linked list values

# Write a function, linked_list_values, that takes in the head of a linked list as an argument. 
# The function should return a list containing all values of the nodes in the linked list.

# Hey. This is our first linked list problem, so you should be liberal with watching the Approach and Walkthrough.
# Be productive! -AZ

      


def linked_list_values(head):
    values = []
    current = head
    
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


def llv_recurse(head):
    values = []
    #create helper fxn for recursion
    fill_values(head, values)
    
    return values



def fill_values(head, values):
    if head is None:
        return
    values.append(head.val)
    fill_values(head.next, values)
    
    