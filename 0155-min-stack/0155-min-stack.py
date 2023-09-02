class MinStack:

    def __init__(self):
        self.min = float('inf')  # how to define infinity
        self.stack = []
        

    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        self.stack.append([val,self.min])

    def pop(self) -> None:
        lastItem = self.stack.pop()[0]
        if len(self.stack) != 0:
            self.min = self.stack[-1][1]
        else:
            self.min = float('inf')
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()