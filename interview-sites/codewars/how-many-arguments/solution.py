# https://www.codewars.com/kata/how-many-arguments/train/python

def args_count(*args, **kwargs):
    return len(args) + len(kwargs)
