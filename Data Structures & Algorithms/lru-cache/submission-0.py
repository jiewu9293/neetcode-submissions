class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        #2 dummynodes lru mru
        #lru before lru right after mru
        #self.left.next lru
        #self.right.prev mru
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left



    def get(self, key: int) -> int:
        #Return the value corresponding to the key if the key exists, otherwise return -1
        if key not in self.cache:
            return -1
        node = self.cache[key]
        #node should be mru
        self.remove(node)
        self.insert_most_recent(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.remove(node)
            self.insert_most_recent(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert_most_recent(node)
    #remove both from hashmap and linkedlist
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    
    def remove(self, node):
        #Unlink node from the list by connecting its prev and next nodes.
        previous_node = node.prev
        next_node = node.next

        previous_node.next = next_node
        next_node.prev = previous_node

    def insert_most_recent(self, node):
        previous_node = self.right.prev

        previous_node.next = node
        node.prev = previous_node

        node.next = self.right
        self.right.prev = node

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
        self.prev = None
        self.next = None


