class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm, m = {}, 0  # implementation with hash map
        for l in s:
            try:
                hm[l] += 1
                ks = list(hm.keys())
                for k in ks:
                    if k != l:
                        del hm[k]
                    else:
                        del hm[k]
                        hm[l] = 1
                        break
            except KeyError:
                hm[l] = 1 # whatever number
                if len(hm) > m:
                    m = len(hm)
        return m