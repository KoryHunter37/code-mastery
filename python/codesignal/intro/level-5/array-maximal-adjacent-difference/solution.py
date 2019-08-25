# https://app.codesignal.com/arcade/intro/level-5/EEJxjQ7oo7C5wAGjE

def arrayMaximalAdjacentDifference(inputArray):
    return max([abs(inputArray[i] - inputArray[i+1]) for i in range(len(inputArray[:-1]))])