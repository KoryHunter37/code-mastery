# https://www.codewars.com/kata/sum-of-digits-slash-digital-root/train/python

def digital_root(n):
    n = str(n)
    while len(n) > 1:
        n = str(sum(int(d) for d in n))
        
    return int(n)
