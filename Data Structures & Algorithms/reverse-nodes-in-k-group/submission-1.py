# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Find the k-th node from If there aren't k nodes left  (leave the rest as-is).
Reverse group
Re-connect the reversed linkedlist back into the list.
Move forward to the next group
group_prev  = dummy first node before current group
group_start = 1  (first node in the current group
kth         = 3   find the k-th node from a group
group_next  = 4 first node after the current group
"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = self.get_kth(group_prev, k)
            #, there are fewer than k nodes left
            if kth is None:
                break
            group_next = kth.next
            group_start = group_prev.next
        #Reverse the current group:
            previous = group_next
            current = group_start

            while current is not group_next:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            
            #Re-connect the reversed segment back into the list.
            group_prev.next = kth
            #prepare for reverse next group
            group_prev = group_start

        return dummy.next



        
    def get_kth(self,current,k):
        while current is not None and k > 0:
            current = current.next
            k -=1 
        return current
