# https://www.codewars.com/kata/dont-give-me-five/train/python

def dont_give_me_five(start,end):
    count = 0
    for i in range(start, end + 1):
        if '5' not in str(i):
            count += 1
            
    return count
