class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while st and st[-1][1] < t:
                prev_i, _ = st.pop()
                res[prev_i] = i - prev_i
            st.append((i, t))
        
        return res