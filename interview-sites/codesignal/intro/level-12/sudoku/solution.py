# https://app.codesignal.com/arcade/intro/level-12/tQgasP8b62JBeirMS

def sudoku(grid):
    GRID_SIZE = 9
    digits = list(range(1, GRID_SIZE + 1))
    
    for row in grid:
        if sorted(row) != digits:
            return False
        
    columns = [[row[i] for row in grid] for i in range(GRID_SIZE)]
    for column in columns:
        if sorted(column) != digits:
            return False
        
    for h in range(0, GRID_SIZE, 3):
        for w in range(0, GRID_SIZE, 3):
            chunk = []
            
            coords = [0, 1, 2]
            for x in coords:
                for y in coords:
                    chunk.append(grid[h+x][w+y])
            
            if sorted(chunk) != digits:
                return False
            
    return True
