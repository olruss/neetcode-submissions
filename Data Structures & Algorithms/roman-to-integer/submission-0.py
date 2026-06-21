class Solution:
    def romanToInt(self, s: str) -> int:
        pairs = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        
        res = 0

        i = len(s) - 1
        while i >= 0:
            if i > 0 and s[i-1:i+1] in pairs:
                res += pairs[s[i-1:i + 1]]
                i -= 2
            else:
                res += pairs[s[i]]
                i -= 1
        return res
