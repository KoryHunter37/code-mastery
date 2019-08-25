# https://app.codesignal.com/arcade/intro/level-5/ZMR5n7vJbexnLrgaM

def minesweeper(matrix):    
        height = len(matrix)
        width = len(matrix[0])

        result = []
        for h in range(height):
                result.append([])

                for w in range(width):
                        # Add a new number indicating the number of mines for this h, w coordinate
                        result[-1].append(0)
                        
                        # These are the combinations of adjacent index values we want to check
                        xi = [-1, 0, 1]
                        yi = [-1, 0, 1]
                        
                        for x in xi:
                                for y in yi:
                                        # Check the ensure validity of space in matrix
                                        if 0 <= h + y < height and 0 <= w + x < width:
                                                # Check to ensure this is a mine in an adjacent field
                                                if not (x == y == 0) and matrix[h+y][w+x]:
                                                        result[-1][-1] += 1
                                                
        return result
      