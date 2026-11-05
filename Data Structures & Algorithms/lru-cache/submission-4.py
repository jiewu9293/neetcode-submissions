class LRUCache:

    def __init__(self, capacity: int):
        # 虚拟头尾节点
        self.head = Node()
        self.tail = Node()
        self.capacity = capacity
        self.cache = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add_to_end(node)
        
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 找到已有节点，并更新它保存的值
            node = self.cache[key]
            node.val = value
        
            self.remove(node)
            self.add_to_end(node)

            return
        node = Node(key, value)
        self.cache[key] = node
        self.add_to_end(node)
        if len(self.cache) > self.capacity:
            least_recent_node = self.head.next
            self.remove(least_recent_node)

            del self.cache[least_recent_node.key]
            

        
    def remove(self, node: Node) -> None:
        previous_node = node.prev
        next_node = node.next

        previous_node.next = next_node
        next_node.prev = previous_node
    
    def add_to_end(self, node: Node) -> None:
        last_node = self.tail.prev
        
        last_node.next = node
        node.prev = last_node

        node.next = self.tail
        self.tail.prev = node



class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None     
