# https://www.codewars.com/kata/find-the-unique-number-1/train/python

def find_uniq(arr):
    nums = []
    
    for number in arr:
        if number in nums:
            main_num = number
            break
        else:
            nums.append(number)
            
    arr = set(arr)
    arr.remove(main_num)
    return arr.pop()