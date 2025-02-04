#  sum of lengths

# Write a function sumOfLengths that takes in a list of strings and returns the total length of the strings.

# You must solve this recursively.  

def sum_of_lengths(arr):
    if len(arr) == 0:
        return 0
    return len(arr[0]) + sum_of_lengths(arr[1:])

print(sum_of_lengths(['goat', 'cat', 'purple']))