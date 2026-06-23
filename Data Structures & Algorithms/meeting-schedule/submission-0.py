"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # first sort them, then just iterate and check for intersections

        intervals.sort(key=lambda i: i.start)
        _prev_end = None
        for i in intervals:
            if _prev_end:
                if i.start < _prev_end:
                    return False
            _prev_end = i.end
        return True