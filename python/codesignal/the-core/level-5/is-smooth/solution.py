# https://app.codesignal.com/arcade/code-arcade/list-forest-edge/3LmZafR9wMCWpdgra

def isSmooth(arr):
    # Odd number of elements
    if len(arr) % 2 != 0:
        middle = arr[len(arr) // 2]
    
    # Even number of elements
    else:
        middle = arr[len(arr) // 2] + arr[len(arr) // 2 - 1]
        
    print(middle)
    return arr[0] == middle == arr[-1]
