from collections import Counter
# The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. 
# Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'

# You can assume that the input only contains alphabetic characters.

# basically just build a string


def compress(s):
    
    s += '!'  # THIS IS ADDED SO THAT YOU HAVE A DIFFERENT CHAR TO TERMINATE T if s[i] == s[j] condition on the last char sequence. 

    
    result = ''
    i = 0
    j = 0
    
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            # result += s[i:j]
            # i = j
            # j += 1
            num = j - i
            
            if num == 1:
                result += s[i]
            else:
                result += str(num) + s[i]
            i = j
            
    return result

print(compress('ccaaatsss'))
            
             
def compress_fast(s):
    
    s += '!'  # THIS IS ADDED SO THAT YOU HAVE A DIFFERENT CHAR TO TERMINATE T if s[i] == s[j] condition on the last char sequence. 

    
    result = []
    i = 0
    j = 0
    
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            # result += s[i:j]
            # i = j
            # j += 1
            num = j - i
            
            if num == 1:
                result.append(s[i])  # WATCH THE += thing, this increases time complexity
            else:
                result.append((num) + s[i])
            i = j # DONT FORGET THINE LINE, terminates the string sequence
            
    return "".append(result)

print(compress('ccaaatsss'))