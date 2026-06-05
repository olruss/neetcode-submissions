
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #    [7,1,7,2,2,4]
        # 7   =   =
        # 6   =   =
        # 5   =   =
        # 4   =   = +   =
        # 3   =   = +   =
        # 2   = + = = = =
        # 1   = = = = = = 

        #   while moving from left to right we can collect rectangles of different heights:
        #   turns:
        #   1. h7 -> rect 7x1
        #   2. h1 -> rect 7x1 truncated to  1x2
        #   3. 7 -> 1x3, 7x1 added as it's higher then prev
        #   4. 2 -> 1x4, 2x2 (7x1 truncated)
        #   5. 2 -> 1x5, 2x3
        #   6. 4 -> 1x6, 2x4, 4x1

        # instead of storing width, we can store just an index
        # check max area only when truncating
        st = []
        max_area = 0
        # [7,1,7,2,2,4]
        # 0 [(7, 0)]
        # 1 [(7, 0), (1, 1)] -> [(1, 0)]
        # 2 [(1, 0), (7, 2)]
        # 3 [(1, 0), (7, 2), (2, 3)] -> [(1, 0), (2, 2)]
        # 4 [(1, 0), (2, 2), (2, 4)] -> [(1, 0), (2, 2)]
        # 

        def area(r, i):
            return r[0] * (i - r[1] + 1)

        def merge(l, r):
            return (min(l[0], r[0]), min(l[1], r[1]))

        for i, h in enumerate(heights):
            st.append((h, i))
            
            while len(st) > 1:
                right, left = st.pop(), st.pop()
                if right[0] > left[0]:
                    st.extend((left, right))
                    break
                # update max area and merge
                max_area = max(
                    max_area,
                    area(left, i - 1)
                )
                st.append(merge(right, left))
            # print(st)

        for r in st:
            a = area(r, len(heights) - 1)
            # print(f"Area of {r} -> {a}")
            max_area = max(
                max_area,
                a
            )
        
        
    

        
        return max_area


