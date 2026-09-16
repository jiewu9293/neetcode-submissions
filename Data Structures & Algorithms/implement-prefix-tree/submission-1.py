class TrieNode:
    def __init__(self):
        self.children = {}
    
        self.is_end = False
class PrefixTree:

    def __init__(self):
        #all words start from root node
        #rootnode is a dummynode
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        #set the final node is_end = True means the end of a word
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            #child node of the char not exist means the word not exist
            if char not in node.children:
                return False
            node = node.children[char]
        #check the last node is the end of the input word 
        return node.is_end


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        #when all characters exist return true directly
        return True
        
        