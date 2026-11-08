class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        
        original_color = image[sr][sc]
        if original_color == color:
            return image
        rows = len(image)
        cols = len(image[0])
        queue = deque([(sr, sc)])

        image[sr][sc] = color
        while queue:
            row, col = queue.popleft()
            for row_change, col_change in directions:
                next_row = row + row_change
                next_col = col + col_change
                if not (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                ):
                    continue
                if image[next_row][next_col] != original_color:
                    continue
                image[next_row][next_col] = color
                queue.append((next_row, next_col))
        return image