# https://app.codesignal.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5

def avoidObstacles(inputArray):

    for i in range(1, max(inputArray) + 1):
        landings = [l for l in range(max(inputArray) + 1) if l % i == 0]

        if len( set(landings) & set(inputArray) ) == 0:
            return i
        
    return max(inputArray) + 1
