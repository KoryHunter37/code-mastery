# https://app.codesignal.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9

from collections import Counter

def low_letter_difference(s1: str, s2: str) -> bool:
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    keys = set(list(c1.keys()) + list(c2.keys()))
    diff = 0
    
    for key in keys:
        c1_value = c1.get(key, None)
        c2_value = c2.get(key, None)
        
        if c1_value is None or c2_value is None:
            diff += c1_value if c1_value is not None else c2_value

        else:
            diff += abs(c1_value - c2_value)
            
        if diff > 1:
            return False
    
    return True
    

def stringsRearrangement(inputArray, record=[]):
    # Initial Iteration
    if record == []:
        
        for i, strng in enumerate(inputArray):
            success, final_record = stringsRearrangement(inputArray[:i] + inputArray[i+1:], [strng])
            if success:
                return final_record
            
    # Recursive Iteration
    elif len(inputArray) > 1:
        last_string = record[-1]
        
        for i, strng in enumerate(inputArray):
            if low_letter_difference(last_string, strng):
                    success, this_record = stringsRearrangement(inputArray[:i] + inputArray[i+1:], record + [strng])
                    if success:
                        return this_record
                    
    # Base Iteration
    else:
        last_string = record[-1]
        
        if low_letter_difference(last_string, inputArray[0]):
            return True, record + inputArray[0]
