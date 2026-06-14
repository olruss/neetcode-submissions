class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # fast-slow pointers
        # we are starting at index 0
        # assuming every number is a node pointing to the next

        fast, slow = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow