# https://app.codesignal.com/arcade/intro/level-8/3AgqcKrxbwFhd3Z3R

def extractEachKth(arr, k):
    return [arr[i] for i in range(len(arr)) if (i+1) % k != 0]
