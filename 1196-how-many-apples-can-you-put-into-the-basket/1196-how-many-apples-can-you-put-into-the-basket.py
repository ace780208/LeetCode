class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        m = 5000
        ans = 0
        for w in weight:
            if w <= m:
                m -= w
                ans += 1
            else:
                break
        return ans