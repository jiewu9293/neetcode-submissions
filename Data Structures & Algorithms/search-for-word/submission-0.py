class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        #The DFS function checks whether the remaining substring word[index:] can be formed starting from board[row][col]
        def dfs(row,col,index):
            #check whether current cell is valid
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            #check if current cell can match  
            if board[row][col] != word[index]:
                return False
            #The last character has been matched successfully.
            if index == len(word) - 1:
                return True
            #mark the cell as visited
            original_char = board[row][col]
            board[row][col] = "#"
            #move to the next level
            #explore the four adjacent directions
            found = (
                dfs(row+1,col,index+1)
                or dfs(row-1,col,index+1)
                or dfs(row,col+1,index+1)
                or dfs(row,col-1,index+1)
            )
            # Restore the cell so other search paths can use it.
            board[row][col] = original_char
            return found
         # Try every cell as the starting position.
        for row in range(rows):
            for col in range(cols):
                if dfs(row,col,0):
                    return True
        return False

        