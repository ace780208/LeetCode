from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapify(heap)
        for pnt in points:
            dist = pnt[0]**2 + pnt[1]**2
            heappush(heap, (-dist, pnt))
            if len(heap) > k:
                heappop(heap)
            
        return [pnt[1] for pnt in heap]
            