from collections import Counter


def most_frequent_char(s):
    count = Counter(s)
    max = None
    
    for char in s:
        if max is None or count[char] > count[max]:
            max = char
            
    return max
print(most_frequent_char('aasafdfgsrgdfasdasfrdhftjhfgsdfgdsfxgb'))