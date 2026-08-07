class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 2)

        for x in range(2, n + 1):
            dp[x] = min(dp[x - 2] + cost[x - 2], dp[x - 1] + cost[x - 1])
        
        dp[n + 1] = dp[n - 1] + cost[n - 1]

        return min(dp[n], dp[n + 1])
        