class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_map = {n: i for i, n in enumerate(nums2)}
        res = [nums2_map[n] for n in nums1]
        return res