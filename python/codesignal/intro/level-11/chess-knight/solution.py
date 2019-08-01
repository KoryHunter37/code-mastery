# https://app.codesignal.com/arcade/intro/level-11/pwRLrkrNpnsbgMndb

from typing import Tuple

def coords(coord: str) -> Tuple[int, int]:
    c1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}.get(coord[0])
    c2 = int(coord[1]) 
    return (c1, c2)


def chessKnight(cell):
    cell = coords(cell)
    moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    
    count = 0
    for move in moves:
        x, y = cell
        
        if 0 < x + move[0] < 9 and 0 < y + move[1] < 9:
            count += 1
            
    return count
