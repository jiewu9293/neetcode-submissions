"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
hashmap two pass 
first pass copy all nodes and store the mapping
{original:copied}
second pass connect next and random pointer in each node in the copied linkedlist
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copied = {
            None:None
        }
        current = head
        while current is not None:
            old_to_copied[current] = Node(current.val)
            current = current.next
        current = head
        #second pass handled next and random pointer
        while current is not None:
            copied_node = old_to_copied[current]
            copied_node.random = old_to_copied[current.random]
            copied_node.next = old_to_copied[current.next]

            current = current.next
        return old_to_copied[head]


        