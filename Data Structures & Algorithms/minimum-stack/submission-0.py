class MinStack:

    st: list[tuple[int, int]]  # element = (value, min_value)

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        self.st.append((val, self._min(val)))

    def pop(self) -> None:
        return self.st.pop()[0]

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]

    def _min(self, val):
        if not self.st:
            return val
        return min(val, self.st[-1][1])
 