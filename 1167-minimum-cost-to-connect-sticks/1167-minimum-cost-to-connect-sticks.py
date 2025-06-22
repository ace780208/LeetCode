from heapq import *
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            first_mini = heappop(sticks)
            sec_mini = heappop(sticks)
            cost += (first_mini + sec_mini)
            heappush(sticks, (first_mini + sec_mini))
        
        return cost