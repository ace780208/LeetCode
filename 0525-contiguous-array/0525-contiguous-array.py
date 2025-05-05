class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = {0: -1}
        curr = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                curr -= 1
            else:
                curr += 1
            
            if curr in counts:
                ans = max(ans, i - counts[curr])
            else:
                counts[curr] = i
        return ans