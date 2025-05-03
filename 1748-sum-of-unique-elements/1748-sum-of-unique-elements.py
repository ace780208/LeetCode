class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = {}
        ans = 0
        for num in nums:
            if num in counts:
                counts[num] = counts.get(num, 0) + 1
                if counts[num] > 2:
                    continue
                ans -= num
            else:
                ans += num
                counts[num] = counts.get(num, 0) + 1
        return ans