# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
"""
 heap always gives us the node with the smallest value on top.
"""
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        min_heap = [] 
        #push each head to minq
        for list_index, node in enumerate(lists):
            if node is not None:
                    heapq.heappush(
                    min_heap,
                    (node.val,list_index,node)
                    )
        
        dummy = ListNode(0)
        tail = dummy
        while min_heap:
            value,list_index,node=heapq.heappop(
                min_heap
            )
            tail.next = node
            tail = tail.next

            if node.next is not None:
                heapq.heappush(
                    min_heap,
                    (   node.next.val,
                        list_index,
                        node.next,
                    )
                )
        return dummy.next
