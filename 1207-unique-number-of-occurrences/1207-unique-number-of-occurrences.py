class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # create a hashmap to store element frequency
        counts = {}
        for i in arr:
            counts[i] = counts.get(i, 0) + 1
        # check whether the number of unique elements and frequency is the same
        return len(counts) == len(set(counts.values()))