class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        for left in range(len(nums)):
            right = left
            while right < len(nums):
                if nums[right] != 0:
                    break
                else:
                    right += 1
            
            if right < len(nums) and nums[right] != 0 :
                nums[left], nums[right] = nums[right], nums[left]
            
        return nums
            
