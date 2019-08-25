# https://www.codewars.com/kata/sudoku-solution-validator/train/python

def validSolution(board):

    # Each Chunk
    for w in range(0, 9, 3):
        for h in range(0, 9, 3):
            
            record = []
            for x in range(w, w+3):
                for y in range(h, h+3):
                    if board[y][x] in record:
                        return False
                    else:
                        record.append(board[y][x])
                        
    # Each Row
    for h in range(0, 9):
        if len(set(board[h])) != 9:
            return False
        if 0 in board[h]:
            return False
            
    # Each Column
    for w in range(0, 9):
        column = [board[h][w] for h in range(0, 9)]
        if len(set(column)) != 9:
            return False
        
    return True
