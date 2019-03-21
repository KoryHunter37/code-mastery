# https://www.codewars.com/kata/valid-parentheses/train/python

def valid_parentheses(string):
    depth = 0
    for p in string:
        depth += {'(': 1, ')': -1}.get(p, 0)
        
        if depth < 0:
            return False
        
    return depth == 0
    