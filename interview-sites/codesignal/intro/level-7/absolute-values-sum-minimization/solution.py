# https://app.codesignal.com/arcade/intro/level-7/ZFnQkq9RmMiyE6qtq

def absoluteValuesSumMinimization(a):
    differences = [ (sum([abs(j - i) for j in a]), i) for i in a]
    return min(differences)[1]
