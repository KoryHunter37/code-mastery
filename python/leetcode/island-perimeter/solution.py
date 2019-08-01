# https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        for y, row in enumerate(grid, 0):
            grid[y].insert(0, 0)
            grid[y].append(0)
            
        grid.insert(0, [0 for x in range(0, len(grid[0]))])
        grid.append([0 for x in range(0, len(grid[0]))])
        
        distance = 0
        for y, row in enumerate(grid, 0):
            for x, col in enumerate(grid[0], 0):
                if grid[y][x] == 1:
                    
                    if grid[y-1][x] == 0:
                        distance += 1
                    if grid[y+1][x] == 0:
                        distance += 1
                    if grid[y][x-1] == 0:
                        distance += 1
                    if grid[y][x+1] == 0:
                        distance += 1
    
        return distance