class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        mf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            mf = max(mf, count[s[r]])

            if r + 1 - l - mf > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r + 1 - l)

        return res