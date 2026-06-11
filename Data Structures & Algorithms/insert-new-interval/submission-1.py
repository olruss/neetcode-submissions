class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # time 1 2 3 4 5 6 7 8 9
        # int1 ---
        # int2.    ----
        # int3.          -----

        # newint.     -----

        # it overlaps with int2 and int3
        # overalps means start date or end date within the int range


        # so we can create a new list to store merged intervals
        # iterate over intervals and check
        # and check if it overlaps with new interval
        # if it does - merge them and continue
        # if not - add to new intervals and also add the rest 
        # as they are not overlaping

        merged = [newInterval]

        def overlaps(int1, int2):
            # [6, 8], [7, 9]
            return (
                int1[0] < int2[0] and int1[1] > int2[1]
                or int2[0] < int1[0] and int2[1] > int1[1]
            )

        def merge(int1, int2):
            return [min(int1[0], int2[0]), max(int1[1], int2[1])]


        for interval in intervals:
            # interval starts after last merged
            if interval[0] > merged[-1][1]:
                merged.append(interval)
            # merged interval starts after interval
            elif merged[-1][0] > interval[1]:
                _int = merged.pop()
                merged.append(interval)
                merged.append(_int)
            else: # need to merge
                merged.append(merge(merged.pop(), interval))
            
        return merged
