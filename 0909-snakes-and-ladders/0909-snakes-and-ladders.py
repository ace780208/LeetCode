from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        end = n**2
        odd = n%2 == 1
        
        def decode(i: int):

            remainder = i%(2*n)
            row = None
            if remainder in (0, n):
                row = n - i//n
            else:    
                row = (n-1) - i//n
                
            col = None
            if not remainder:
                col = 0
            elif remainder > n:
                col = 2*n - remainder
            else:
                col = remainder - 1
            
            return (row, col)
        
        queue = deque([(None, 1)])
        seen = set()
        seen.add((None, 1))
        '''
        row, col = decode(1)
        if board[row][col] != -1:
            prev_start, prev_end = queue.popleft()
            curr_end = board[row][col]
            queue.append((prev_end, curr_end))
            seen.add((prev_end, curr_end))
        '''    
        roll = 0
        
        ladder = False
        while queue:
            square_cnt = len(queue)
            roll += 1
            for sq in range(square_cnt):
                prev_start, prev_end = queue.popleft()
                for dice_roll in range(1, 7):
                    curr_end = prev_end + dice_roll
                    if curr_end > end:
                        break
                    row, col = decode(curr_end)
                    if board[row][col] != -1:
                        curr_end = board[row][col]
                    if curr_end == end:
                        return roll
                        
                    if (prev_end, curr_end) not in seen:
                        seen.add((prev_end, curr_end))
                        queue.append((prev_end, curr_end))
            
        return -1
                        
