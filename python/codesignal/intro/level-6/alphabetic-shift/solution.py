# https://app.codesignal.com/arcade/intro/level-6/PWLT8GBrv9xXy4Dui

def alphabeticShift(inputString):
    result = []
    for i, letter in enumerate(inputString):
        index = (ord(letter) - 97 + 1) % 26 + 97
        result.append(chr(index))
        
    return ''.join(result)