class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # build a graph where key is a bomb and value are a list of bomb the key bomb can detonate
        graph = dict()
        bomb_cnt = len(bombs)
        for i in range(bomb_cnt):
            if i not in graph:
                graph[i] = []
            for j in range(i+1, bomb_cnt):
                if j not in graph:
                    graph[j] = []
                if i!=j:
                    dist = (bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2 
                    if bombs[i][2]**2 >= dist:
                        graph[i].append(j)
                    
                    if bombs[j][2]**2 >= dist:
                        graph[j].append(i)
                        
        
        def dfs(node):
            for affected in graph[node]:
                if affected not in seen:
                    seen.add(affected)
                    dfs(affected)
        
        ans = 0
        for i in range(bomb_cnt):
            seen = set()
            seen.add(i)
            dfs(i)
            ans = max(len(seen), ans)
        
        return ans
                        