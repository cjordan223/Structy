# ZIPPER LIST

# Write a function, zipper_lists, that takes in the head of two linked lists as arguments. 
# The function should zipper the two lists together into single linked list by alternating nodes. 
# If one of the linked lists is longer than the other, the resulting list should terminate with the 
# remaining nodes. The function should return the head of the zippered linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty.



class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def zipper_lists(head_1, head_2):
  # use a two pointer approach
  # alternate between lists by using count even/odd a condition
  # once you exhaust all options, you can just print the remainder of the other list
    tail = head_1
    current_1 = head_1.next
    current_2 = head_2
    
    count = 0
    
    while current_1 is not None and current_2 is not None:
      if count % 2 == 0:
        tail.next =  current_2
        current_2 =  current_2.next
        
      else:
        tail.next = current_1
        current_1 = current_1.next 
      tail = tail.next 
      count += 1
      
    
    if current_1 is not None:
      tail.next = current_1
      
    if current_2 is not None:
      tail.next = current_2
        
    
    
    return head_1
    
    
    # Helper function to print the linked list
def print_list(head):
      current = head
      while current is not None:
        print(current.val, end=" -> ")
        current = current.next
      print("None")

    # Test cases
a = Node('a')
b = Node('b')
c = Node('c')
a.next = b
b.next = c

x = Node('x')
y = Node('y')
z = Node('z')
x.next = y
y.next = z

    # Zipper the lists
result = zipper_lists(a, x)
print_list(result)

    # Another test case
p = Node(1)
q = Node(2)
r = Node(3)
p.next = q
q.next = r

m = Node(4)
n = Node(5)

    # Zipper the lists
result = zipper_lists(p, m)
print_list(result)

    

    
  
  
  
    