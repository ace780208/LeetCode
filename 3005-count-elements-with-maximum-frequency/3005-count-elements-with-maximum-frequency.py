class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = {}
        max_freq = 0
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            max_freq = max(max_freq, counts[num])
        
        ans = 0
        for index, e in counts.items():
            if e == max_freq:
                ans += e
        
        return ans