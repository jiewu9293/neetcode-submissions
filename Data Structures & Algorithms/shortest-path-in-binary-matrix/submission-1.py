
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1 
        directions = [(-1,-1),(-1,0),(-1,1),
                        (0,-1),   (0,1),
                        (1,-1), (1,0), (1,1)]
        queue = deque([(0,0,1)])
        visited = {(0,0)}
        
        while queue:
            r,c,length = queue.popleft()
            if r == n -1 and c == n - 1:
                return length

            for rc,cc in directions:
                nr,nc = r +rc, c + cc
                if(0<= nr <n
                    and 0<= nc <n
                    and grid[nr][nc] != 1
                    and not (nr,nc) in visited):
                    visited.add((nr,nc))
                    queue.append((nr,nc,length + 1)) 
        return -1


        