# https://www.codewars.com/kata/credit-card-mask/train/python

# return masked string
def maskify(cc):
    return '#' * (len(cc)-4) + cc[-4:]
