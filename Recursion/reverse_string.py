# Write a function, reverse_string, that takes in a string as an argument. 
# The function should return the string with its characters in reverse order. You must do this recursively.

def reverse_string(s):
    # keep in mind the gial of recursion is to reduce your problem size
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]#<---  call recursively with reduced problem size then concatenating
    # return s[::-1]

print(reverse_string("conner"))
    
    