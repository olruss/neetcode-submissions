class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotated = {
            "0": "0",
            "1": "1",
            "6": "9",
            "9": "6",
            "8": "8"
        }

        new = []
        for v in str(n)[::-1]:
            if v not in rotated:
                return False
            new.append(rotated[v])
        return str(n) != "".join(new)
