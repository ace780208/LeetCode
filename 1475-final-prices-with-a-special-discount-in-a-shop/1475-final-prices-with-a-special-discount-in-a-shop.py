class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # this is the typical monotonic increase problem for recording price index
        # create a stack to record price index
        stack = []
        ans = [0] * len(prices)
        for i in range(len(prices)):
            # calculate discount price if the later index is first met
            while stack and prices[i] <= prices[stack[-1]]:
                prev_idx = stack.pop()
                ans[prev_idx] = prices[prev_idx] - prices[i]

            stack.append(i)
        # populate the rest price where discount does not apply
        while stack:
            idx = stack.pop()
            ans[idx] = prices[idx]

        return ans