# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
slow moves one step at a time
fast moves two steps at a time
If the list has no cycle, the fast pointer will reach the end (null) and the loop stops.
f the list has a cycle, the fast pointer will eventually meet slow

"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # Checking if Fast Pointer Can Advance Safely
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
#use is not equal 2 different nodes can have same val
            if slow is fast:
                return True
        return False


