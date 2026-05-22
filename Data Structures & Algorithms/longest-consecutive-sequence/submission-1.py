class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        d = {}
        s = set(nums)
        max_len = 1
        curr_len = 1

        for x in s:
            if x - 1 not in s:
                curr_num = x
                curr_len = 1
                
                while curr_num + 1 in s:
                    curr_num += 1
                    curr_len += 1
                
                max_len = max(max_len, curr_len)
        
        return max_len

