class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }

        for t in tokens:
            if t in operations:
                b, a = operands.pop(), operands.pop()
                res = operations[t](a, b)
                operands.append(res)
            else:
                operands.append(int(t))
        assert len(operands) == 1
        return round(operands.pop())