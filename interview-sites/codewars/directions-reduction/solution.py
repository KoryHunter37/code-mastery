# https://www.codewars.com/kata/directions-reduction/train/python

import copy

def dirReduc(arr):
    print(arr)
    new_arr = copy.copy(arr)
    opposites = {"NORTH":"SOUTH", "SOUTH":"NORTH", "WEST":"EAST", "EAST":"WEST"}
    
    while True:
        for i in range(len(new_arr) - 1):
            curr = new_arr[i]
            next = new_arr[i+1]
            
                continue
                
            if opposites.get(curr) == next:
                new_arr[i], new_arr[i+1] = "SKIP", "SKIP"
        
        if "SKIP" in new_arr:
            new_arr = [e for e in new_arr if e != "SKIP"]
        else:
            break
        
    print(new_arr)
    return new_arr