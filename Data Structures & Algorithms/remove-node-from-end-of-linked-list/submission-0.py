# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Use two pointers so that the gap between them is exactly n
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = head

        #Move the fast pointer n steps ahead first.
        for _ in range(n):
            fast = fast.next

        #Then move both pointers together.
        #When the fast pointer reaches the end, the slow pointer will be just before the node we must remove.
        while fast is not None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
#  we can't return head because head can be removed
        return dummy.next

