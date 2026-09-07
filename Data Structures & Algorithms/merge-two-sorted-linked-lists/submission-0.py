# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        dummy 虚拟头节点
        Using a dummy node as head of merged linkedlist
        move tail alone the merged linkedlist
        return the head of the new sorted linked list.
        """
        dummy = ListNode(0)
        tail = dummy
        #while both linkedlist we have nodes
        #Pick the smaller node.
        #
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next 
            else:
                #connect list2 to end of merged list
                tail.next = list2
                #move list2 to its next node
                list2 = list2.next
            #move tail to newly added node
            tail = tail.next
        #when one of the linkedlist is none 
        # If list1 still has nodes, attach its remaining nodes
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next
