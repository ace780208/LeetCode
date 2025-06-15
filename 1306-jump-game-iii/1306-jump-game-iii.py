from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        arr_len = len(arr)
        def jump(node):
            jump_stop = []
            if node + arr[node] < arr_len:
                jump_stop.append(node+arr[node])
            if node - arr[node] >= 0:
                jump_stop.append(node - arr[node])
            
            return jump_stop
        
        queue = deque([start])
        seen = set()
        seen.add(start)
        
        while queue:
            node = queue.popleft()
            if arr[node] == 0:
                return True
            
            for stop in jump(node):
                if stop not in seen:
                    seen.add(stop)
                    queue.append(stop)
            
        
        return False