# Write a function, factorial, that takes in a number n and returns the factorial of that number. The factorial of n is the product of all the positive numbers less than or equal to n. You must solve this recursively.

# For example, the factorial of 6 is:

# 6 * 5 * 4 * 3 * 2 * 1 = 720

# You can assume that n is a non-negative integer. Note that the factorial of 0 is defined to be 1 (wiki).



# consider factorial of 1, or 0 equals 1



def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(4))