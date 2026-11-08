from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        island_count = 0 
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != "1":
                    continue
                island_count += 1
                queue = deque([(row, col)])
                grid[row][col] = "0"

                while queue:
                    current_row, current_col = queue.popleft()
                    for row_change,col_change in directions:
                        next_row = current_row + row_change
                        next_col = current_col + col_change

                        if not (0<=next_row<rows and 0<=next_col<cols):
                            continue
                        if grid[next_row][next_col] != "1":
                            continue
                        grid[next_row][next_col] = "0"
                        queue.append((next_row,next_col))
        return island_count

                
                

