class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(curr, curr_sum, curr_d):
            if len(curr) == k:
                if curr_sum == n:
                    ans.append(curr.copy())
                return
            
            for d in range(curr_d, 10):
                if (curr_sum + d) <= n:
                    curr.append(d)
                    backtrack(curr, curr_sum + d, d+1)
                    curr.pop()
        
        for i in range(1, 10):
            backtrack([i], i, i+1)
        
        return ans