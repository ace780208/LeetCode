class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # get the dimension of matrix
        m = len(matrix)
        n = len(matrix[0])
        # cache each grid for the current falling sum
        @cache
        def dp(row, col):
            if row==0:
                return matrix[row][col]

            # get the current grid value
            curr_sum = matrix[row][col]
            if row > 0:
                # get the minimal path sum from previous row
                min_path = dp(row-1, col)
                if col-1 >= 0:
                    min_path = min(min_path, dp(row-1, col-1))
                if col+1 < n:
                    min_path = min(min_path, dp(row-1, col+1))
            
            curr_sum += min_path
            return curr_sum
        
        ans = float("inf")
        for c in range(n):
            ans = min(ans, dp(m-1, c))
        
        return ans