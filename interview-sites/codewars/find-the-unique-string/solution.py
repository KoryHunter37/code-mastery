# https://www.codewars.com/kata/find-the-unique-string/train/python

def find_uniq(arr):
    set_arr = [str(sorted(set(word.casefold() + " "))) for word in arr]
    
    a, b = set(set_arr)
    
    if set_arr.count(a) > set_arr.count(b):
        search = b
    else:
        search = a
        
    return [word for word in arr if str(sorted(set(word.casefold() + " "))) == search][0]