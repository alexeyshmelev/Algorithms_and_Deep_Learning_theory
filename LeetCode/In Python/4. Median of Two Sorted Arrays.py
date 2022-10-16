from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        all = sorted(nums1 + nums2)
        l = len(all) // 2
        if len(all) % 2:
            return all[l]
        else:
            return (all[l - 1] + all[l]) / 2
