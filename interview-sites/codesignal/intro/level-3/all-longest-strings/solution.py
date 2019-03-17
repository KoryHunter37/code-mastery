# https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL

def allLongestStrings(inputArray):
    max_length = max([len(i) for i in inputArray])
    return [i for i in inputArray if len(i) == max_length]
    