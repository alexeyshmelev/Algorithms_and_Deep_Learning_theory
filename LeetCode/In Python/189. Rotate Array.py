from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = -k%len(nums)
        nums[:] = nums[c:] + nums[:c]
