# https://app.codesignal.com/arcade/intro/level-8/rRGGbTtwZe2mA8Wov

def firstDigit(inputString):
    for letter in inputString:
        if letter.isdigit():
            return letter
        