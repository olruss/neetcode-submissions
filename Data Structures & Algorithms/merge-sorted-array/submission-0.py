class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted([*nums1[:m], *nums2])[:]
        # i1, i2 = m - 1, n - 1

        # while i1 >= 0 or i2 >= 0:
        #     if nums1[i1] > nums2[i2]:
        #         n = nums1[i1]
        #         i1 -= 1
        #     else:
        #         n = nums2[i2]
        #         i2 -= 1
        #     nums1[i1 + i2 + 1] = n
        
