class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        freq, window = Counter(t), {}
        have, need = 0, len(freq)
        res, resLen = [-1, -1], float('inf')

        l = 0
        while l < len(s) and s[l] not in freq:
            l += 1
        
        
        for r in range(l, len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in freq and window[c] == freq[c]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res, resLen = [l, r], (r - l + 1)
                
                window[s[l]] -= 1

                if s[l] in freq and window[s[l]] < freq[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""