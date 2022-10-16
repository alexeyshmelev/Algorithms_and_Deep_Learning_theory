class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        p = r // 2
        while r > l:
            if nums[p] == target:
                return p
            elif target > nums[p]:
                l = p + 1
                p = (r - l) // 2 + l
            else:
                r = p
                p = (r - l) // 2 + l
        return -1