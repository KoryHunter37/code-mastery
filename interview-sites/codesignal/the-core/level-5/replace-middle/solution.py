# https://app.codesignal.com/arcade/code-arcade/list-forest-edge/APD5T5CybxTtfkdjL

from typing import List

def replaceMiddle(arr: List[int]) -> List[int]:
    if len(arr) % 2 == 0:
        m1 = len(arr) // 2 - 1
        m2 = len(arr) // 2
        arr[m1] = sum(arr[m1:m2+1])
        del arr[m2]
        
    return arr
