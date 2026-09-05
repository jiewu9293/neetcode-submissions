class MinStack:
    #O(1)
    # (val,current_min)
    # each time push elem to stack we need to update currentmin
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            current_min = val
        else:
            #chooese the smaller val as current min
            current_min = min(val,self.stack[-1][1])
        self.stack.append(
            (val,current_min)
        )
            
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
