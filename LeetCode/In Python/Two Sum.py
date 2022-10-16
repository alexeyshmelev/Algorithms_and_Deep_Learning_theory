from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # метод двух указателей
        nums_sorted = sorted(nums)
        cond = True
        a = 0
        b = len(nums) - 1
        while cond:
            if nums_sorted[a] + nums_sorted[b] == target:
                l = nums.index(nums_sorted[a])
                nums.pop(l)
                r = nums.index(nums_sorted[b])
                if r >= l:
                    r += 1
                return [l, r]
            elif nums_sorted[a] + nums_sorted[b] < target:
                a += 1
            elif nums_sorted[a] + nums_sorted[b] > target:
                b -= 1
