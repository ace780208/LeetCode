class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # create hashmap to store the values and their frequency
        counts = {}
        for i in arr:
            counts[i] = counts.get(i, 0) + 1

        # create a hashset to check whether the frequency is unique
        freq = set()
        for key, val in counts.items():
            if val in freq:
                return False
            else:
                freq.add(val)
        
        return True