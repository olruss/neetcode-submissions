from collections import deque

class MyStack:

    def __init__(self):
        self.st = deque()
        self.buf = deque()

    def push(self, x: int) -> None:
        self.buf.append(x)
        for _ in range(len(self.st)):
            self.buf.append(self.st.popleft())
        self.st, self.buf = self.buf, self.st

    def pop(self) -> int:
        return self.st.popleft()

    def top(self) -> int:
        return self.st[0]
        

    def empty(self) -> bool:
        return not self.st
# 1, 2, 3     
# [1] [2] -> [] [2, 1]
# add to empty, then put from empty to 

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()