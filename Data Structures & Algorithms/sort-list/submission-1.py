# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        right_head = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(right_head)

        return self.merge(left, right)

    def merge(self,left,right):
        dummy = ListNode(0)
        tail = dummy
        while left is not None and right is not None:
            if left.val <= right.val:
                tail.next= left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

            if left is not None:
                tail.next = left
            else:
                tail.next = right
            
        return dummy.next
            


