class Solution:

    devider = "||-||"
    empty = "empty"

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return self.empty
        return self.devider.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == self.empty:
            return []
        return s.split(self.devider)
            