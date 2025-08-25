class MinStack:

    def __init__(self):
        self.stk=[]
        self.mstk=[]

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.mstk) == 0:
            self.mstk.append(val)
        else:
            self.mstk.append(min(val,self.mstk[-1]))

    def pop(self) -> None:
        self.stk.pop()
        self.mstk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.mstk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()