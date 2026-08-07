class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 3:
            return max(nums)

        dp1 = [0] * (n-1)
        dp2 = [0] * (n-1)

        dp1[0] = nums[0]
        dp1[1] = dp2[0] = nums[1]
        dp1[2] = dp1[0] + nums[2]
        dp2[1] = nums[2]
        dp2[2] = dp2[0] + nums[3]

        for x in range(3, n - 1):
            dp1[x] = max(dp1[x-3] + nums[x], dp1[x-2] + nums[x])
            dp2[x] = max(dp2[x-3] + nums[x+1], dp2[x-2] + nums[x+1])

        return max(dp1[n-2], dp1[n-3], dp2[n-2], dp2[n-3])