from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankset = set(bank)
        
        def mutation(node):
            ans = []
            gene = ['A', 'C', 'G', 'T']
            for i in range(len(node)):
                for j in gene:
                    if j == node[i]:
                        continue
                    tmp = list(node)
                    tmp[i] = j
                    tmp = ''.join(tmp)
                    if tmp in bankset:
                        ans.append(tmp)
            return ans
        
        queue = deque([(startGene, 0)])
        seen = set()
        seen.add(startGene)
        while queue:
            node, step = queue.popleft()
            if node == endGene:
                return step
            
            for mut in mutation(node):
                print(mut)
                if mut not in seen:
                    seen.add(mut)
                    queue.append((mut, step + 1))
                    
        return -1
                