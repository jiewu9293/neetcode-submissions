# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
minq tail insertion
 heap always gives us the node with the smallest value on top.
tail always point to the end of the linkedlist 
dummy node to return the result linkedlist

"""
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        for list_index,node in enumerate(lists):
            if node is not None:
                heapq.heappush(
                    minheap,
                    (node.val,list_index,node)
                )
        dummy = ListNode(0)
        tail = dummy
        while minheap:
            value,list_index,node = heapq.heappop(minheap)
            tail.next= node
            tail = tail.next

            if node.next is not None:
                heapq.heappush(
                    minheap,
                    (node.next.val,
                    list_index,
                    node.next)
                )
        
        return dummy.next        