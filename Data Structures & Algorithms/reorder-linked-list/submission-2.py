# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return 
        
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        current = slow.next
        slow.next = None
        previous = None 

        while current is not None:
            next_node = current.next

            current.next = previous

            previous = current

            current = next_node

        first = head
        second = previous

        while second is not None:
            first_next = first.next
            second_next = second.next

            first.next =  second
            second.next =  first_next

            first = first_next
            second = second_next
        
