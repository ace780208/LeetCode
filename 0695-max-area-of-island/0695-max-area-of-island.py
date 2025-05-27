class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        graph = dict()
        seen = set()
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        
        def valid(i, j):
            return 0 <= i < m and 0 <= j < n and grid[i][j] == 1
        
        ans = 0
        for row in range(m):
            for col in range(n):
                curr = 0
                if (row, col) not in seen and grid[row][col] == 1:
                    curr += 1
                    def dfs(row, col):
                        nonlocal curr
                        for dx, dy in neighbors:
                            new_row, new_col = row + dx, col + dy
                            if valid(new_row, new_col) and (new_row, new_col) not in seen:
                                curr += 1
                                seen.add((new_row, new_col))
                                dfs(new_row, new_col)
                                
                    seen.add((row, col))
                    dfs(row, col)

                ans = max(ans, curr)
                
        return ans