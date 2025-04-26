class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        ans = -1
        for key, val in counts.items():
            if val == 1:
                ans = max(ans, key)
        return ans