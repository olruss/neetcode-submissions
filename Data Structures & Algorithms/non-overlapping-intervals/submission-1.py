class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 1 - - - 5
        #     3 - - - 7
        #         5 6
        #             7 - - 9
        # here we need to remove one interval (3-7)
        # this looks streightforward: if we remove first overlaping
        # interval - we win

        # but lets find another case
        # 1 - - - 5
        #   2 - 4
        #       4 - - 6
        # if we follow same logic,
        # then we sill remove two intervals
        # when we need to remove one (1-5)
        # so need to find another approach
        # 
        # let's try to sort them by end time
        # and see what we'll get
        #  1 2 3 4 5 6
        #    2 - 4
        #  1 - - - 5
        #        4 - 6
        # works. lets try our previous example
        # 1 2 3 4 5 6 7 8 9
        # 1 - - - 5
        #         5 6
        #     3 - - - 7
        #             7 - 9
        # again, works
        # seems we found the solution
        # but why it works?
        # because when we sort by start date,
        # we don't know the end date. so this interval
        # shadows other intervals
        # sorting by end date prevents it

        intervals.sort(key = lambda x: x[1])

        cnt = 0
        last = None
        for i in intervals:
            if last is None:
                last = i
                continue
            # overlaps if i.start is < last.end
            if i[0] < last[1]:
                cnt += 1  # assume we removed it
            else:
                last = i
        
        return cnt

        # 1 2
        #   2  4
        # 1    4

