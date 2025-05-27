class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seen = set()
        graph = dict()
        
        for i in range(n):
            graph[i] = []
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        def dfs(node):
            if node not in seen:
                seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        dfs(source)
        
        return destination in seen