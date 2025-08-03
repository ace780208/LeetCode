class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        for box, unit in boxTypes:
            if truckSize == 0:
                break
                
            if truckSize >= box:
                truckSize -= box
                ans += box*unit
            elif truckSize < box:
                ans += truckSize * unit
                truckSize = 0
        
        return ans