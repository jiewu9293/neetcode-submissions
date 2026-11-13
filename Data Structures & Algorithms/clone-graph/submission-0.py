"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        copies = {}
        def clone(old_node):
            if old_node in copies:
                return copies[old_node]
            new_node = Node(old_node.val)

            copies[old_node] = new_node
            for old_neighbor in old_node.neighbors:
                new_neighbor = clone(old_neighbor)
                new_node.neighbors.append(new_neighbor)
            return new_node
        return clone(node)