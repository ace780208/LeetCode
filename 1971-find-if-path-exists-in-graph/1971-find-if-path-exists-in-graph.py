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
            seen.add(node)
            if node == destination: 
                seen.add(node)
                return True
            for neighbor in graph[node]:
                if neighbor not in seen:
                    print(neighbor)
                    seen.add(neighbor)
                    if dfs(neighbor):
                        return True
            
            return False
        
        return dfs(source)