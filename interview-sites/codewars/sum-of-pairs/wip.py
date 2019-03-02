# https://www.codewars.com/kata/sum-of-pairs/train/python

from itertools import combinations

def sum_pairs(ints, s):

    best_index = float("inf")
    best_pair = None
    
    for i in range(len(ints)):
        for j in range(i+1, len(ints)):
            if ints[i] + ints[j] == s:
                if j < best_index:
                    best_index = j
                    best_pair = [ints[i], ints[j]]
                    
    return best_pair

#     sums = [(i, j) for i, j in combinations(ints, 2) if i + j == s]
#     indices = [(i, j) for i, j in combinations(range(len(ints)), 2) if ints[i] + ints[j] == s]
    
#     if len(sums) == 0:
#         return None
        
#     return None
#     def sort(pair):
#         pass
    
        
#     return list( sorted( sums, key=lambda sum: max(indices[sums.index(sum)]) )[0] )
        