from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, s = 0, len(nums) - 1, []
        while l <= r:
            ln = abs(nums[l])
            rn = abs(nums[r])
            if ln >= rn:
                s.append(ln ** 2)
                l += 1
            else:
                s.append(rn ** 2)
                r -= 1
        return s[::-1]
