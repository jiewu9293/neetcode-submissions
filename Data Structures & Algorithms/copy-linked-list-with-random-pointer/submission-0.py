"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
Hash Map (Two Pass)
Pass 1: Create a copy of every node (just values), and store the mapping:
original_node → copied_node
Pass 2: Use this map to connect next and random pointers for each copied node.
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = {
            None: None,
        }
        current = head
        while current is not None:
            old_to_copy[current] = Node(current.val)
            current = current.next

        current = head
        while current is not None:
            copied_node = old_to_copy[current]
            copied_node.next = old_to_copy[current.next]
            copied_node.random = old_to_copy[current.random]

            current = current.next
        return old_to_copy[head]