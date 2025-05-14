class NumArray:

    def __init__(self, nums: List[int]):
        # create initialization nums, size, and calculate the prefix sum
        self.nums = nums
        self.prefix = [0]
        for i in range(len(self.size)):
            self.prefix.append(self.prefix[-1] + self.nums[i])

    def sumRange(self, left: int, right: int) -> int:
        # count the inclusive moving sum
        return (self.prefix[right + 1] - self.prefix[left])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)