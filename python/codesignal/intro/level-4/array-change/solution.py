# https://app.codesignal.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg

def arrayChange(inputArray):
    
    count = 0
    for i, n in enumerate(inputArray):
        # First index will always be increasing
        if i == 0:
            continue
            
        if n <= inputArray[i-1]:
            diff = abs(inputArray[i-1] - n) + 1
            inputArray[i] += diff
            count += diff
            
    return count
