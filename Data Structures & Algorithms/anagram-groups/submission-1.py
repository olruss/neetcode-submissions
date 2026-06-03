class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def anagram_key(s: str):
            store = [0] * 26
            ord_a = ord('a')
            for l in s:
                store[ord(l) - ord_a] += 1
            return tuple(store)
        res = {}
        for s in strs:
            k = anagram_key(s)
            if k in res:
                res[k].append(s)
            else:
                res[k] = [s]

        return list(res.values())