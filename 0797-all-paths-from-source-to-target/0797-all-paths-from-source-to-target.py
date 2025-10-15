class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def backtrack(path):
            if path[-1] == len(graph)-1:
                ans.append(path.copy())
                return
            
            for node in graph[path[-1]]:
                if node not in path:
                    path.append(node)
                    backtrack(path)
                    path.pop()
                    
        backtrack([0])
        return ans