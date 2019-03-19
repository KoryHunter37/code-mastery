# https://app.codesignal.com/arcade/intro/level-5/ZMR5n7vJbexnLrgaM

def minesweeper(matrix):    
        height = len(matrix)
        width = len(matrix[0])

        result = []
        for h in range(height):
                result.append([])

                for w in range(width):
                        above_left  = matrix[h-1][w-1] if h-1 >= 0 and w-1 >= 0        else None
                        above       = matrix[h-1][w  ] if h-1 >= 0                     else None
                        above_right = matrix[h-1][w+1] if h-1 >= 0 and w+1 < width     else None

                        same_left   = matrix[h  ][w-1] if w-1 >= 0                     else None
                        same_right  = matrix[h  ][w+1] if w+1 < width                  else None

                        below_left  = matrix[h+1][w-1] if h+1 < height and w-1 >= 0    else None
                        below       = matrix[h+1][w  ] if h+1 < height                 else None
                        below_right = matrix[h+1][w+1] if h+1 < height and w+1 < width else None

                        adjacents = [above_left, above, above_right, same_left, same_right, below_left, below, below_right]

                        result[-1].append(len([i for i in adjacents if i]))

        return result
      