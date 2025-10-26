class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}
        def dp(ith_step):
            # top down dynamic programming
            
            if ith_step in memo:
                return memo[ith_step]
            
            memo[ith_step] = dp(ith_step-1) + dp(ith_step - 2)
            return memo[ith_step]
            
        return dp(n)