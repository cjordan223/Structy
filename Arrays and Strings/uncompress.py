# write a function, uncompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern:

# <number><char>

# for example, '2c' or '3a'.

# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.


def uncompress(s):
    
    numbers = '123456789'
    result = ''
    i = 0
    j = 0
    
    while j < len(s):
        # if s[j] is a numeric character
        if s[j] in numbers: 
            j += 1
        else:
            thing = s[i:j] # slice s at index i up to (not including) j
            num = int(thing) # showing this step visibilty, int(x) converts to a variable
            
            result += s[j] * num #######THIS INCREASES TIME CMPLEXITY - string concatenation
            
            j += 1
            i = j
            
    return result
    
    
print(uncompress("2c3a1t")) # -> 'ccaaat'
uncompress("4s2b") # -> 'ssssbb'
uncompress("2p1o5p") # -> 'ppoppppp'



############ YOU CAN ALSO SOLVE THIS WITH A LIST, 
def uncompres_fast(s):
    
    numbers = '123456789'
    result = []
    i = 0
    j = 0
    
    while j < len(s):
        # if s[j] is a numeric character
        if s[j] in numbers: 
            j += 1
        else:
            thing = s[i:j] # slice s at index i up to (not including) j
            num = int(thing) # showing this step visibilty, int(x) converts to a variable
            
            result.append(s[j] * num) #######THIS INCREASES TIME CMPLEXITY - string concatenation
            
            j += 1
            i = j
            
    return ''.join(result)


print(uncompress("2c3a1t")) # -> 'ccaaat'
uncompress("4s2b") # -> 'ssssbb'
uncompress("2p1o5p") # -> '