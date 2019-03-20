# https://app.codesignal.com/arcade/intro/level-6/t97bpjfrMDZH8GJhi

from typing import List

def chessBoardCellColor(cell1, cell2):
    
    # Function to turn coordinate pair of capital letter and digit into indices
    def get_coords(cell: str) -> (int, int):
        return (ord(cell[0]) - 65, int(cell[1]) - 1)
        
        
    c1x, c1y = get_coords(cell1)
    c2x, c2y = get_coords(cell2)
    
    
    # Function to generate a list of lists where the truth value of a cell indicates the cell's color
    def get_board() -> List[List[bool]]:
        board = []
        
        for y in range(8):
            board.append([])
            for x in range(8):
                board[-1].append((y + x) % 2 == 0)    
                
        return board
                
            
    board = get_board()
    
    return board[c1y][c1x] == board[c2x][c2y]
            