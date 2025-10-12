class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(sub_sum):
            total_subs = 1
            curr_sum = 0
            for i in nums:
                if curr_sum + i <= sub_sum:
                    curr_sum += i
                else:
                    curr_sum = i
                    total_subs += 1
            return total_subs <= k
        
        left = max(nums)
        right = sum(nums)
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
                
                