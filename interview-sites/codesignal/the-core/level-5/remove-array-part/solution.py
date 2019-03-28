# https://app.codesignal.com/arcade/code-arcade/list-forest-edge/vPJB7T28fyCeh2Ljn

from typing import List

def removeArrayPart(arr: List[int], l: int, r: int) -> List[int]:
    del arr[l: r+1]
    return arr
