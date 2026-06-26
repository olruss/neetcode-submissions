class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        def col(i):
            return "".join(word[i] for word in words if len(word) > i)
        
        for i, word in enumerate(words):
            if word != col(i):
                return False
        
        return True