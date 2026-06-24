import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # use min heap. each entry - room
        # [(meeting end time, room_number, count), ...]
        # we will  add entries until size of heap < n
        # then we will pop and add even, modifying it end date
        # if it starts earlier then meeting ends
        # and update the count - number of rooms being used

        available = [
            (0, room_number, 0)
            for room_number in range(n)
        ]
        busy = []

        for m in sorted(meetings):
            while busy and busy[0][0] <= m[0]:
                room = heapq.heappop(busy)
                heapq.heappush(available, (0, room[1], room[2]))

            if available:
                room = heapq.heappop(available)
            else:
                room = heapq.heappop(busy)
            heapq.heappush(
                busy,
                (   
                    # adjusted end time
                    m[1] + max(0, room[0] - m[0]),
                    # room number
                    room[1],
                    # number of usage
                    room[2] + 1,
                )
            )

        max_room = max(busy, key=lambda r: (r[2], -r[1]))
        return max_room[1]