class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                area = 0
                grid[row][col] = 0
                stack = [(row,col)]
                while stack:
                    r,c = stack.pop()
                    area += 1

                    for rc,cc in directions:
                        nr,nc = r + rc, c + cc 

                        if not (0<=nr<rows and 0<=nc<cols):
                            continue
                        if grid[nr][nc] == 0:
                            continue
                        
                        grid[nr][nc] = 0
                        stack.append((nr,nc))
                max_area = max(max_area,area)
        return max_area


