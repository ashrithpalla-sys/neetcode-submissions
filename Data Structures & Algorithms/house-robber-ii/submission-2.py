class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 3:
            return max(nums)
        
        def rob1(nums: List[int]) -> int:
            n = len(nums)

            if n <= 2:
                return max(nums)

            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = nums[1]
            dp[2] = dp[0] + nums[2]

            for x in range(3, n):
                dp[x] = max(dp[x-3] + nums[x], dp[x-2] + nums[x])
            
            return max(dp[n-2], dp[n - 1])
        
        return max(rob1(nums[:-1]), rob1(nums[1:]))