class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #use a mark at terminal node
        END = "$"
        trie = {}
        #insert each target word into trie
        for word in words:
            #start from rootnode
            node = trie
            #create node in trie for the char if node not exist then move to the node
            for char in word:
                node = node.setdefault(char,{})
            #at the terminal node store complete word, allow to  add to result 
            node[END] = word
        #seach path in board and traverse trie at same time 
        result = []
        rows = len(board)
        cols = len(board[0])
        def dfs(row,col,parent):
            char = board[row][col]
            #move to the character node in trie
            node = parent[char]
            #check if the node is the terminal node 
            word = node.pop(END,None)

            if word is not None:
                result.append(word)
            #mark current cell as visited
            board[row][col] = "#"
             #explore the four adjacent directions
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                next_row = row + dr
                next_col = col + dc
                #check next position is within board
                #check next character is in trie if not we can prune
                
                if(0<=next_row<rows and 
                0<=next_col<cols and 
                board[next_row][next_col] in node):
                #run dfs on next character
                    dfs(next_row,next_col,node)
                
            #restore current cell so other branch can visit the cell
            board[row][col] = char
            #remove the node if it is empty
            if not node:
                parent.pop(char)
        #if the character in trie run dfs from the cell
        for row in range(rows):
            for col in range(cols):
                if board[row][col] in trie:
                    dfs(row,col,trie)
        return result            


                
                

            
            


        
        
                