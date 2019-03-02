# https://www.codewars.com/kata/are-they-the-same/train/python

def comp(array1, array2):
    
    # Check for None inputs
    if array1 is None or array2 is None:
        return False
       
    # Check for uneven inputs
    if len(array1) != len(array2):
        return False
        
    array1, array2 = sorted(array1), sorted(array2)
    
    
    return all( [array1[i] ** 2 == array2[i] for i in range(len(array1))] )