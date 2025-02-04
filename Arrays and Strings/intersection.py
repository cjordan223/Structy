def intersection(a, b):
  new_arr = []
  
  for item in a:
      if item in b:
          new_arr.append(item)

  return new_arr



print(intersection([4,2,1], [1,2,4,6])) # -> [1,2,4]

    
    
    
    
# use a set to decrease time complexity!!!

def intersection_fast(c,d):
    result = []
    items = set()
    
    for item in c:
        items.add(item) 
        
    for ely in d:
        if ely in items:
            result.append(ely)
        
    return items   
    
    
print(intersection_fast([4,2,1], [1,2,4,6])) # -> [1,2,4]




# cleaner version with python features


def intersection_clean(c,d):
    result = []
    items = set(c)


        
    for ely in d:
        if ely in items:
            result.append(ely)
        
    return items   
    
    
print(intersection_clean([4,2,1], [1,2,4,6])) # -> [1,2,4]

# Ultra PYTHONIC

def intersection_clean(c,d):
    items = set(c)
    return sorted([ely for ely in d if ely in items])

print(intersection_clean([4,2,1], [1,2,4,6])) # -> [1,2,4]
