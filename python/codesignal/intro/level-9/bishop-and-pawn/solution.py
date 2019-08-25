# https://app.codesignal.com/arcade/intro/level-9/6M57rMTFB9MeDeSWo

from typing import Tuple

def coords(coord: str) -> Tuple[int, int]:
    c1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}[coord[0]]
    c2 = int(coord[1])
    return (c1, c2)

def bishopAndPawn(bishop: str, pawn: str) -> bool:
    bishop, pawn = coords(bishop), coords(pawn)
    return abs(bishop[0] - pawn[0]) == abs(bishop[1] - pawn[1])
