"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        p_cnt = {}
        for i in intervals:
            p_cnt[i.start] = p_cnt.get(i.start, 0) + 1
            p_cnt[i.end] = p_cnt.get(i.end, 0) - 1
        
        points = sorted(p_cnt.keys())

        res = 0
        cnt = 0
        for p in points:
            cnt += p_cnt[p]
            res = max(res, cnt)
        
        return res