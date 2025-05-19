from collections import deque
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        idx_hash = {}
        for right in range(len(nums)):
            if nums[right] not in idx_hash:
                idx_hash[nums[right]] = deque()
                idx_hash[nums[right]].append(right)
            else:
                idx_hash[nums[right]].append(right)
            print(idx_hash[nums[right]])
            while len(idx_hash[nums[right]]) > k:
                min_left = idx_hash[nums[right]].popleft()
                left = max(left, min_left + 1)
            ans = max(ans, right - left + 1)
        return ans