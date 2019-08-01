# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/KeMqde6oqfF5wBXxf

def arrayPacking(a):
    result = []
    for n in a[::-1]:
        r = bin(n).replace('b', '').rjust(8, '0')
        result.append(r[-8:])
       
    return int(''.join(result), 2)
