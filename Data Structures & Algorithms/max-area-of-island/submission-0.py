class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                stack = [(row, col)]
                grid[row][col] = 0

                area = 0
                while stack:
                    current_row, current_col = stack.pop()
                    area += 1
                    for dr, dc in directions:
                        next_row = current_row + dr
                        next_col = current_col + dc

                        if not(0<=next_row<rows and 0<=next_col<cols):
                            continue

                        if grid[next_row][next_col] == 0:
                            continue
                        grid[next_row][next_col] = 0
                        stack.append((next_row, next_col))
                max_area = max(max_area, area)
        return max_area