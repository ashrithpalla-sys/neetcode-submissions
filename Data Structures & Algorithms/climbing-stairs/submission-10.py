class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for x in range(4, n+1):
            dp[x] = dp[x - 1] + dp[x - 2]

        return dp[n]