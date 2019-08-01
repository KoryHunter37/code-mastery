# https://www.codewars.com/kata/are-they-the-same/train/python

def comp(array1, array2):
    try:    
        array1, array2 = sorted(array1), sorted(array2)
        return all( [array1[i] ** 2 == array2[i] for i in range(len(array1))] )
    except:
        return False