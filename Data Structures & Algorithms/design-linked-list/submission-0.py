class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
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
        
        new_node = Node(val)

        new_node.next = previous.next

        previous.next = new_node

        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        previous = self.dummy
        for _ in range(index):
            previous = previous.next
        previous.next = previous.next.next

        self.size -= 1
class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)