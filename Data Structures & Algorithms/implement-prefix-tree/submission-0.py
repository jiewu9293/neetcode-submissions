class TrieNode:
    def __init__(self):
        #key is the character value is the node
        self.children = {}

        #if the character is the end of a word 
        self.is_end = False
class PrefixTree:

    def __init__(self):
        # dummynode
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        #Start from the root.
        node = self.root
        for char in word:
            #if node not exist create node
            if char not in node.children:
                node.children[char] = TrieNode()
            #move to child
            node = node.children[char]
        #After processing all characters,   mark endOfWord = true.
        node.is_end = True
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        #After processing all characters, check if the node is end
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        