class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom-up dynamic programming

        cost_len = len(cost)
        dp = [0] * (cost_len + 1)

        for idx in range(2, cost_len+1):
            dp[idx] = min(dp[idx-1]+cost[idx-1], dp[idx-2]+cost[idx-2])
        
        return dp[len(cost)]