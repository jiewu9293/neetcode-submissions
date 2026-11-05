class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.dummy = Node()

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1 
        current = self.dummy.next
        for _ in range(index):
            current = current.next
        return current.val
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
 
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        previous = self.dummy

        for _ in range(index):
            previous = previous.next
        newNode = Node(val)
        newNode.next = previous.next
        previous.next = newNode
        
        self.size+=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        previous = self.dummy

        for _ in range(index):
            previous = previous.next
        
        previous.next = previous.next.next

        self.size-=1
        




        
class Node:
    def __init__(self,val=0,next_node=None):
        self.val = val
        self.next = next_node


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)