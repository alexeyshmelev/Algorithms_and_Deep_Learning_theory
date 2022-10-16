# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        p = r // 2
        while r > l:
            if isBadVersion(p):
                r = p
                p = (r - l) // 2 + l
            else:
                l = p + 1
                p = (r - l) // 2 + l
        return p