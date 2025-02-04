# fibonacci

# Write a function, fibonacci, that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

# The 0-th number of the sequence is 0.

# The 1-st number of the sequence is 1.

# To generate further numbers of the sequence, calculate the sum of previous two numbers.

# You must solve this recursively.

# recall fib = 0 + 1 + (0 + 1) + (1 + 1) + (2 + 1) + (3 + 2) + (5 + 3)....continue adding prev 2 #'s by themselves
#There are 2 recursive calls within the fxn m

# The time complexity is 2^n   
# The space complexity is just n i.e. the hieight of the recursion tree. you are contanstly 
# returning input to the call stack while your calling for new values, so it never exceeds the height of the tree

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    
    
print(fibonacci(9))