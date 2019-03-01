def is_palindrome(input_string):
    x = list(input_string)
    
    for i in range(0, len(x)):
        compare_index = len(x) - 1 - i
        
        if compare_index <= i:
            return True
        if x[i] != x[compare_index]:
            return False
    
    return True
    
