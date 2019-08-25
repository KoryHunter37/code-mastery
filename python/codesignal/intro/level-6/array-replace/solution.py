# https://app.codesignal.com/arcade/intro/level-6/mCkmbxdMsMTjBc3Bm

def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if i == elemToReplace else i for i in inputArray]
