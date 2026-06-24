"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sweep but store point in times in array
        # +1 - start, -1 - end
        # then for intervals [start, end) sort by end first
        # for [start, end] -> end goes before start

        points = []
        for i in intervals:
            points.append((i.start, 1))
            points.append((i.end, -1))
        
        points.sort(key=lambda p: (p[0], p[1]))

        cnt = 0
        res = 0
        for _, c in points:
            cnt += c
            res = max(res, cnt)
        
        return res