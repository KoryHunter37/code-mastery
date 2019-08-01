# https://app.codesignal.com/interview-practice/task/SKZ45AF99NpbnvgTn

from typing import List

def sudoku2(grid: List[List[str]]) -> bool:
    
    def find_duplicates(nums: List[str]) -> bool:
        return len(nums) != len(set(nums))
    
    
    for row in grid:
        row_nums = [x for x in row if x.isdigit()]
        if find_duplicates(row_nums): 
            return False
        
    for col in range(len(grid[0])):
        col_nums = [grid[y][col] for y in range(len(grid)) if grid[y][col].isdigit()]
        if find_duplicates(col_nums): 
            return False
        
    for y in range(0, len(grid), 3):
        for x in range(0, len(grid[0]), 3):
            chunk_nums = [grid[y+y2][x+x2] for y2 in range(3) for x2 in range(3) if grid[y+y2][x+x2].isdigit()]
            if find_duplicates(chunk_nums): 
                return False
    
    return True
