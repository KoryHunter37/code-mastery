# https://app.codesignal.com/arcade/code-arcade/list-forest-edge/ND8nghbndTNKPP4Tb

from typing import List

def firstReverseTry(arr: List[int]) -> List[int]:
    try:
        arr[0], arr[-1] = arr[-1], arr[0]
    finally:
        return arr
