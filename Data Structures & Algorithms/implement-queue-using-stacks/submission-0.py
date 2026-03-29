class MyQueue:

    def __init__(self):
        self.s = []
        self.temp = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        for i in range(len(self.s) - 1, 0, -1):
            self.temp.append(self.s.pop())
        deleted = self.s.pop()

        for i in range(len(self.temp) - 1, -1, -1):
            self.s.append(self.temp.pop())
        
        return deleted

    def peek(self) -> int:
        for i in range(len(self.s) - 1, -1, -1):
            self.temp.append(self.s.pop())
        peeked = self.temp[-1]

        for i in range(len(self.temp) - 1, -1, -1):
            self.s.append(self.temp.pop())
        
        return peeked

    def empty(self) -> bool:
        return len(self.s) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()