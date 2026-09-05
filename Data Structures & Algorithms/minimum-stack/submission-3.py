class MinStack:
    # O(1)
    # each ele (value, current_min)
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # first elem is the min value
        if not self.stack:
            current_min = val
        # update current min when push elem
        # choose a smaller val as current min
        else:
            current_min = min(
                val,self.stack[-1][1]
            )
        self.stack.append(
            (val,current_min)
        )

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
