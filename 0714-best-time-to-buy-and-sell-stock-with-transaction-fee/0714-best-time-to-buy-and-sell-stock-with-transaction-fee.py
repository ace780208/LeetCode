class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''
        @cache
        def dp(i, holding):
            if i == len(prices):
                return 0
            
            # case for skipping trading this price
            ans = dp(i+1, holding)
            
            if holding:
                # case for selling the stock at the current price
                ans = max(ans, dp(i+1, False)+prices[i]-fee)
            else:
                # case for buying the stock at the current price
                ans = max(ans, dp(i+1, True)-prices[i])
            
            return ans
        
        return dp(0, False)
        '''
        # create a list to store the output of dynamic programing for max profit per state
        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for holding in range(2):
                ans = dp[i+1][holding]
                if holding:
                    ans = max(ans, dp[i+1][0]+prices[i]-fee)
                else:
                    ans = max(ans, dp[i+1][1]-prices[i])
                
                dp[i][holding] = ans
        
        return dp[0][0]
        