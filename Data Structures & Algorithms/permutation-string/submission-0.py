class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import copy
        if len(s1) > len(s2):
            return False

        freq = {}

        for c in s1:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        l = 0
        i = 0
        r = len(s1) - 1
        freq_copy = copy.deepcopy(freq)

        while r < len(s2) and i <= r:
            if s2[i] not in freq_copy or freq_copy[s2[i]] == 0:
                freq_copy = copy.deepcopy(freq)
                l += 1
                i = l
                r += 1
            else:
                freq_copy[s2[i]] -= 1
                result = not any(freq_copy.values())
                if result:
                    return result
                i += 1
        
        return False


