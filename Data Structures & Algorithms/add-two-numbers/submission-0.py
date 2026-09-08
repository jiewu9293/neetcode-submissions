# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
carry
→ Store the carry from the previous digit
dummy node / sentinel node
→ Make it easier to build and return the result linked list
Simulate grade-school addition
→ Process the numbers digit by digit
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #tail at the end of the linkedlist
        #dummy used to return result
        # while → 检查是否还有任何内容需要计算
        #if 检查某一条链表能否安全地向后移动
        carry = 0
        dummy = ListNode(0)
        tail = dummy
        while l1 is not None or l2 is not None or carry:
            value1 = l1.val if l1 is not None else 0
            value2 = l2.val if l2 is not None else 0

            total = value1 + value2 + carry
            digit = total % 10
            carry = total // 10
        #create a node and have tail connect to it 
            tail.next = ListNode(digit)
            tail = tail.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return dummy.next

