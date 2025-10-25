class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        def backtrack(curr):
            if len(curr) == n:
                ans.append(int(''.join(curr)))
                return
            
            lower = int(curr[-1]) - k
            upper = int(curr[-1]) + k
            for d in set([lower, upper]):
                if d >= 0 and d<10:
                    curr.append(str(d))
                    backtrack(curr)
                    curr.pop()
        
        for i in range(1, 10):
            backtrack([str(i)])
        
        return ans