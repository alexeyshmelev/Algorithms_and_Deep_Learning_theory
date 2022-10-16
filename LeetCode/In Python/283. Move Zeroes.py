from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = [*filter(lambda a: a != 0, nums)] + [0] * nums.count(0)
