class Solution:
    sep = "#"

    def encode(self, strs: List[str]) -> str:
        # corner cases:
        # 1) strs = [] -> ""
        # 2) strs = [""] -> "0#"
        # 3) strs = ["abc", "", "def"] -> "3#abc0#3#def"
        parts = []
        for s in strs:
            parts.append(f"{str(len(s))}#{s}")
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        # corner cases:
        # 1) "" -> []
        # 2) "0#" -> 
        l, r = 0, 0
        res = []
        while l < len(s):
            # read the length of the next word until separator (#)
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            # read the word. r is now pointing to "#", so l should shift to r + 1
            l = r + 1
            letters = []
            for _ in range(length):
                if l >= len(s):
                    break
                letters.append(s[l])
                l += 1
            res.append("".join(letters))
            r = l
        return res
