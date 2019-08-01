# https://app.codesignal.com/arcade/intro/level-12/uRWu6K8E7uLi3Qtvx

from enum import Enum

class Dir(Enum):
    R = (1, 0)
    D = (0, 1)
    L = (-1, 0)
    U = (0, -1)


def spiralNumbers(n):
    values = list(range(1, n**2 + 1))
    result = [[None for x in range(n)] for y in range(n)]

    x1, y1 = 0, 0
    direction = Dir.R.value
    result[y1][x1] = values.pop(0)

    while len(values) > 0:
        x2, y2 = x1 + direction[0], y1 + direction[1]

        # If the proposed coordinate is valid
        if 0 <= x2 < n and 0 <= y2 < n and result[y2][x2] is None:
            x1, y1 = x2, y2
            result[y1][x1] = values.pop(0)
        else:
            if direction == Dir.R.value:
                direction = Dir.D.value
            elif direction == Dir.D.value:
                direction = Dir.L.value
            elif direction == Dir.L.value:
                direction = Dir.U.value
            elif direction == Dir.U.value:
                direction = Dir.R.value

    return result
