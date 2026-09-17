class Solution:
    """
    first build a Trie containing all words,
    run DFS on the board while using the Trie for prefix pruning.
    搜索网格时，如果当前路径不是任何单词的前缀，就立即停止。
    At the terminal node, I store the complete word instead of just a boolean flag. This allows me to add the word directly to the result
    """
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        END = "$"
        trie = {}
        # Build the Trie.
        for word in words:
            node = trie

            for char in word:
                node = node.setdefault(char,{})
            # Store the complete word at the terminal node.
            node[END] = word
        
        rows = len(board)
        cols = len(board[0])
        result = []
        """
        pass in the parent Trie node and use the board character to move to the corresponding child.
        """
        def dfs(row,col,parent):
            char = board[row][col]
            
            node = parent[char]
            word = node.pop(END, None)
            if word is not None:
                result.append(word)

            # Mark the current cell as visited.
            #cell can not be reused within same path
            board[row][col] = "#"

            #explore the four adjacent directions
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + dr
                next_col = col + dc
                if(0 <= next_row < rows
                and 0 <= next_col < cols
                #check whether the next character exists in the current Trie node. If it does not, prefix pruning
                and board[next_row][next_col] in node):
                    dfs(next_row, next_col, node)

                 # Restore the current cell during backtracking.
            board[row][col] = char

            if not node:
                parent.pop(char)
             # Start DFS only when the cell can match a Trie prefix.
        for row in range(rows):
            for col in range(cols):
                if board[row][col] in trie:
                    dfs(row, col, trie) 
        return result                   
                    



