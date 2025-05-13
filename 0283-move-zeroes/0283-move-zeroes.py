class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for left in range(len(nums)-1):
            if nums[left] != 0:
                continue
            
            right = left + 1
            while nums[right] == 0 and right < len(nums) - 1:
                right += 1
                continue
            
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

            
        