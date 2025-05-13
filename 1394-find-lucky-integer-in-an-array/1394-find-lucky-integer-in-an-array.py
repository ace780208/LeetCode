class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # create a hashmap to store the frequency of a value in the arr
        counts = {}
        for val in arr:
            counts[val] = counts.get(val, 0) + 1

        # loop the hashmap to find the maximum lucky integer
        ans = -1
        for key, freq in counts.items():
            if key == freq:
                ans = max(ans, key)
        return ans