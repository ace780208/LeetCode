class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(num + prefix[-1])

        ans = -1
        for index, left in enumerate(prefix[:-1]):
            right = prefix[-1] - prefix[index+1]
            if left == right:
                ans = index

        return ans

