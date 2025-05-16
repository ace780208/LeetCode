class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(prices)
        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                prev_idx = stack.pop()
                ans[prev_idx] = prices[prev_idx] - prices[i]

            stack.append(i)
        
        while stack:
            idx = stack.pop()
            ans[idx] = prices[idx]

        return ans