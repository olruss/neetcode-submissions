import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # use min heap. each entry - room
        # [(meeting end time, room_number, count), ...]
        # we will  add entries until size of heap < n
        # then we will pop and add even, modifying it end date
        # if it starts earlier then meeting ends
        # and update the count - number of rooms being used

        h = [
            (0, room_number, 0)
            for room_number in range(n)
        ]

        for m in sorted(meetings):
            vacant_rooms = []
            while h and h[0][0] <= m[0]:
                room = heapq.heappop(h)
                vacant_rooms.append((0, room[1], room[2]))
            
            for room in vacant_rooms:
                heapq.heappush(h, room)

            room = heapq.heappop(h)
            heapq.heappush(
                h,
                (   
                    # adjusted end time
                    m[1] + max(0, room[0] - m[0]),
                    # room number
                    room[1],
                    # number of usage
                    room[2] + 1,
                )
            )

        max_room = max(h, key=lambda r: (r[2], -r[1]))
        # max_room = None
        # for room in h:
        #     if max_room is None:
        #         max_room = room
        #     elif room[2] > max_room[2]:
        #         max_room = room
        #     elif room[2] == max_room[2] and room[1] < max_room[1]:
        #         max_room = room
        return max_room[1]