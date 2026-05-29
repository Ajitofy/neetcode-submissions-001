class MinStack:

    def __init__(self):
        self.stack=[]       

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None        

    def getMin(self) -> int:
        minimum=float('inf')
        for i in self.stack:
            minimum=min(i,minimum)
        return minimum

