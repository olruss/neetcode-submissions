class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # definition of overlaping intervals:
        # a--------b
        #     c--------d
        #          a--------b
        # a <= d & c <= b
        def overlaps(int1, int2):
            a, b = int1[0], int1[1]
            c, d = int2[0], int2[1]
            return a <= d and c <= b

        def merge(int1, int2):
            return [min(int1[0], int2[0]), max(int1[1], int2[1])]
        
        def stream(intervals):
            prev_int = None

            for interval in intervals:
                if prev_int is None:
                    prev_int = interval
                    continue
                if overlaps(prev_int, interval):
                    prev_int = merge(prev_int, interval)
                else:
                    yield prev_int
                    prev_int = interval
            
            if prev_int:
                yield prev_int
        
        st = stream(sorted(intervals))

        return list(st)
            
