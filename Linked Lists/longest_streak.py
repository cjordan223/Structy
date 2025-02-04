# longest streak

# Write a function, longest_streak, that takes in the head of a linked list as an argument.
# The function should return the length of the longest consecutive streak of the same value within the list.


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):
    # if head is None:
    #     return 0

    # count = 1
    max_count = 1
    # current = head

    # while current.next is not None:
    #     if current.val == current.next.val:
    #         count += 1
    #         if count > max_count:
    #             max_count = count
    #     else:
    #         count = 1
    #     current = current.next

    return max_count