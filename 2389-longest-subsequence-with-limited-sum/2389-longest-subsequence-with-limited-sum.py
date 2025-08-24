class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binary_search(sortlist, target):
            left = 0
            right = len(sortlist)
            while left < right:
                mid = (left + right) //2
                if sortlist[mid] > target:
                    right = mid
                else:
                    left = mid+1

            return left

        
        nums.sort()
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(num+prefix_sum[-1])
        
        #print(prefix_sum)
        ans = []
        for q in queries:
            ans.append(binary_search(prefix_sum, q)-1)
        
        return ans
