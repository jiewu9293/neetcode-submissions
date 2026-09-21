class Solution:
    #save mark explore restore
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        #return true if start from board[row][col] can match word[index:]
        def dfs(row,col,index):
            #check current cell is valid
            if row < 0 or row >= rows or col < 0 or col >=cols:
                return False
            
            if board[row][col] != word[index]:
                return False
            
            #if last character of the word is matched
            if index == len(word) - 1:
                return True
            #current character is matched
            char = board[row][col]
            #mark
            board[row][col] = "#"
            #move to the next level
            #explore 4 other adjacent directions
            found = (
                dfs(row+1,col,index+1) 
                or dfs(row,col+1,index+1)
                or dfs(row-1,col,index+1)
                or dfs(row,col-1,index+1)
            )
            #restore the character so that other search path can use it 
            board[row][col] = char
            return found
        #run dfs on every cell as starting position
        for row in range(rows):
            for col in range(cols):
                if dfs(row,col,0):
                    return True
        return False


                
            