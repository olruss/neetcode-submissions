class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1 2 3 4 5 6 7 8 9 10
        # 3     2
        #       3   2
        #             3 2
        #                    [32]

        # 0 1 2 3 4 5 6 7 8 9 10
        # 1 2     2     1
        #   1   2      2  1
        #     1     2     2 1
        #       1      2     [21]


        # collect cars in list of tuples
        # sort by position
        # go from left to right
        # check arival time
        # if it's less or equal to slowest car - > it's fleet
        # if not - start new fleet

        # cars = []
        # for i in range(len(position)):
        #     cars.append[
        #         (
        #             position[i],
        #             speed[i],
        #             (target-position[i]) / speed[i]
        #         )
        #     ]
        
        # cars.sort(key=lambda x: x[0], reverse=True)
        track = [0] * 1000

        for i in range(len(position)):
            track[position[i]] = (target-position[i]) / speed[i]

        fleets = 0
        slowest_in_fleet = 0
        for i in range(len(track) - 1, -1, -1):
            time = track[i]
            if time == 0:
                continue
            
            if slowest_in_fleet == 0:
                fleets += 1
                slowest_in_fleet = time
                continue
            if time > slowest_in_fleet:
                fleets += 1
                slowest_in_fleet = time
        return fleets
                
            