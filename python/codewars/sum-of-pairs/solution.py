# https://www.codewars.com/kata/sum-of-pairs/train/python

def sum_pairs(ints, s):
    record = set()

    for int in ints:
        complement = s - int
    
        if complement in record:
            return [complement, int]
        
        record.add(int)
        