class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False

        a1 = [0] * 26
        a2 = [0] * 26

        for i in s1:
            a1[ord(i) - 97] += 1  # 97 - unicode of letter 'a'
        for i in range(n1):
            a2[ord(s2[i]) - 97] += 1  # first window

        if a1 == a2:
            return True

        for i in range(n1, n2):  # sliding window
            a2[ord(s2[i - n1]) - 97] -= 1
            a2[ord(s2[i]) - 97] += 1
            if a1 == a2:
                return True
        return False
