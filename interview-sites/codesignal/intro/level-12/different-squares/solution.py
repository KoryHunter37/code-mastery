# https://app.codesignal.com/arcade/intro/level-12/fQpfgxiY6aGiGHLtv

from typing import List

def differentSquares(m: List[List[int]]) -> int:
    height = len(m)
    width = len(m[0])
    
    record = set((m[h][w], m[h][w+1], m[h+1][w], m[h+1][w+1]) for h in range(height-1) for w in range(width-1))
                
    return len(record)
