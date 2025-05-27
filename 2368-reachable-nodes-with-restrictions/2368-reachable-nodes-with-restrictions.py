class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = dict()
        seen = [False] * n
        seen[0] = True
        ans = 1
        for node in restricted:
            seen[node] = True
        for i in range(n):
            graph[i] = []
            
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node):
            nonlocal ans
            for neighbor in graph[node]:
                if not seen[neighbor]:
                    ans += 1
                    seen[neighbor] = True
                    dfs(neighbor)
            
        dfs(0)
        return ans
                    