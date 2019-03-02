# https://www.codewars.com/kata/which-are-in/train/python

def in_array(array1, array2):          
    return sorted({word for word in array1 if any(word in other_word for other_word in array2)})