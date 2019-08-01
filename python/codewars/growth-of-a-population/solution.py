# https://www.codewars.com/kata/growth-of-a-population/train/python

def nb_year(p0, percent, aug, p):
    count = 0

    while p0 < p:
        p0 = p0 * (1 + (percent/100)) + aug
        count += 1
    
    return count
