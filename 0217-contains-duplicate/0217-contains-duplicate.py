class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] >= 2:
                return True
        
        return False