from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapify(heap)
        for i in nums:
            heappush(heap, i)
            if len(heap) > k:
                heappop(heap)
        
        return heappop(heap)