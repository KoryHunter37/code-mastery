# https://app.codesignal.com/arcade/intro/level-9/AACpNbZANCkhHWNs3

def longestDigitsPrefix(inputString):
    
    for i, letter in enumerate(inputString):
        if not letter.isdigit():
            return inputString[:i]
        
    return inputString
