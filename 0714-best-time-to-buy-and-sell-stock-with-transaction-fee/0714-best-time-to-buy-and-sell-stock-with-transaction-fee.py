class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
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