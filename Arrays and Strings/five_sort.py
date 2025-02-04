# five sort

# Write a function, five_sort, that takes in a list of numbers as an argument. 
# The function should rearrange elements of the list such that all 5s appear at the end. 
# Your function should perform this operation in-place by mutating the original list. The function should return the list.

# Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the list.


def five_sort(nums):

# dont bother with brute force, we know it works
# use a two pointer approach
    # word = str(s) # YOU CANT MODIFY A STRING IN PLACE
    
    left = 0
    right = len(nums) - 1  # -1 for boundary
    
    while left < right:
        if nums[right] == 5: # if pointer is 5 already, keep going
            right -= 1
        elif nums[left] == 5: #otherwise, move thru the left side until you hit a 5
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        left += 1
        
    return nums




print(five_sort([5, 1, 5, 3, 5, 2]))  # Output: [2, 1, 3, 5, 5, 5]