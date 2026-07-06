class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        uc = set()
        l = 0
        r = 0
        uc.add(s[l])
        c = 1
        m = 0

        while r + 1 < len(s):
            if s[r + 1] not in uc:
                r += 1
                uc.add(s[r])
                c += 1
            else:
                m = max(m, c)
                while s[l] != s[r + 1]:
                    uc.remove(s[l])
                    l += 1
                uc.remove(s[l])
                l += 1
                c = r - l + 1

        m = max(m, c)
        return m
