class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        st = []
        for p in s:
            if p in pairs:
                st.append(p)
            else:
                if not st or p != pairs[st.pop()]:
                    return False
        return not st