class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        orig_city = set()
        for path in paths:
            orig_city.add(path[0])
        
        for path in paths:
            if path[1] not in orig_city:
                return path[1]
        