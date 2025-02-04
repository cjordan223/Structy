# a function calls itself

def countdown(n):   
    if n == 0:
        return 
    print(n)
    return countdown(n-1)
    
countdown(9)
def sumNumbersRecursive(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sumNumbersRecursive(numbers[1:])

# Example usage:
print(sumNumbersRecursive([1, 2, 3, 4, 5]))  # Output: 15