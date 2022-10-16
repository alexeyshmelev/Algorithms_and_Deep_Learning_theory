from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hm = {}
        for i in nums:
            try:
                hm[i].append(hm[i][-1] + 1)
            except KeyError:
                hm[i] = [0]
        return sum([sum(s) for s in hm.values()])