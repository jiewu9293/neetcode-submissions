class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        minutes = 0
        while queue and fresh > 0:
            current_fruit_num = len(queue)

            for _ in range(current_fruit_num):
                row,col = queue.popleft()

                for dr,dc in directions:
                    nr,nc = row + dr, col + dc

                    if not (0<=nr<rows and 0<=nc<cols):
                        continue
                    if grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
            minutes += 1

        if fresh == 0:
            return minutes
        else:
            return -1 
            