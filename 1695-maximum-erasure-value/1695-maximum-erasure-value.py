class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counts = dict()
        left = 0
        ans = 0
        curr = 0
        for right in range(len(nums)):
            curr += nums[right]
            counts[nums[right]] = counts.get(nums[right], 0) + 1
            while counts[nums[right]] > 1:
                curr -= nums[left]
                counts[nums[left]] -= 1
                left += 1
            ans = max(ans, curr)

        return ans