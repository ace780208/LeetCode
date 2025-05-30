from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([(entrance[0], entrance[1])])
        seen = set()
        seen.add((entrance[0], entrance[1]))
        m = len(maze)
        n = len(maze[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] == '.'
        
        def is_exit(row, col):
            return (row == 0 or row == m-1 or col == 0 or col == n-1) and maze[row][col] == '.'
        
        steps = 0
        while queue:
            cell_counts = len(queue)
            steps += 1
            for _ in range(cell_counts):
                cell_x, cell_y  = queue.popleft()
                for dx, dy in directions:
                    move_x = cell_x + dx
                    move_y = cell_y + dy
                    if valid(move_x, move_y) and (move_x, move_y) not in seen:
                        if is_exit(move_x, move_y):
                            return steps
                        else:
                            queue.append((move_x, move_y))
                            seen.add((move_x, move_y))
                            
        return -1