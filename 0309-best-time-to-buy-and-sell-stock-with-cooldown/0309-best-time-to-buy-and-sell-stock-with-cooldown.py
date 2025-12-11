class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, holding, cd):
            # base case: no profit when reach to the end of prices
            if i >= len(prices):
                return 0
            
            ans = dp(i+1, holding, cd)
            
            if holding:
                # case to compare sell it or hold to the next round
                ans = max(ans, dp(i+1, False, True)+prices[i])
            else:
                # case to constrain cd if sold it in the previous index
                if cd:
                    ans = dp(i+1, False, False)
                else:
                    ans = max(ans, dp(i+1, True, False)-prices[i])
            
            return ans
        return dp(0, False, False)