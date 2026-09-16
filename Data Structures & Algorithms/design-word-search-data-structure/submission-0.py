class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
        #marks the end of a word
        node.is_end = True
    """
    dfs(index, node) checks whether the remaining substring word[index:] can be matched starting from the current Trie node
    """
    def search(self, word: str) -> bool:
        def dfs(index,node):
            # If the entire pattern has been matched,
            # check whether the current node marks the end of a word.
            if index == len(word):
                return node.is_end

            char = word[index]
            #for regular char
            if char != ".":
                # No matching child means the pattern cannot be matched.
                if char not in node.children:
                    return  False
                # Continue matching the next character.
                return dfs(index+1,node.children[char])
            # For the wildcard '.', try every child node.
            for child in node.children.values():
                # Return True if any branch matches the remaining pattern.
                if dfs(index+1,child):
                    return True
            # None of the branches matched.
            return False
        return dfs(0,self.root)
            
        
class TrieNode:
    def __init__(self):
        # Maps each character to its child Trie node
        self.children = {}
        #Indicates whether this node marks the end of a word
        self.is_end = False      
