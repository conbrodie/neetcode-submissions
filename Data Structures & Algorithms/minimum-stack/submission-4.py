class MinStack:
    # 2, 0
    # [1,2,0,6]
    # [1,0]
 
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        if self.stack: 
            self.stack.append(val)
            if self.minStack and val <= self.minStack[-1]:
                self.minStack.append(val)
        else:
            self.stack.append(val)
            self.minStack.append(val)

    def pop(self) -> None:
        if self.top() == self.minStack[-1]:
            self.minStack.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    

