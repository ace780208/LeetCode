from heapq import *
import math
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        while k>0:
            heappush(piles, -math.ceil(abs(heappop(piles))/2))
            k-=1
        
        return abs(sum(piles))