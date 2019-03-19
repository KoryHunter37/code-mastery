# https://app.codesignal.com/arcade/intro/level-5/veW5xJednTy4qcjso

def isIPv4Address(inputString):
    try:
        arr = [int(n) for n in inputString.split(".")]
    except:
        return False
    
    if len(arr) != 4:
        return False
    
    return all([0 <= n <= 255 for n in arr])
    