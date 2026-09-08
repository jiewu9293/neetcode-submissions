# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
use slow and fast to find middle 
When fast reaches the end, slow will be at the midpoint.
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 1. 找中点并断开链表
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        #bread connection
        slow.next = None
        # 2. 反转后半段
        prev = None 

        while second:
            next_node = second.next
            second.next= prev
            prev = second
            second = next_node
        # Merge the two lists:
        #Take a node from first half.
#Take a node from the reversed second half.

        first = head
        second = prev
        while second:
            first_next = first.next
            second_next = second.next    

            first.next = second
            second.next = first_next   

            first = first_next
            second = second_next
        