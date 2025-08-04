class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        threshold = len(arr)//2
        counts = Counter(arr)
        ordered = sorted(counts.values())
        print(ordered)
        ans = 0
        while threshold>0:
            threshold -= ordered.pop()
            ans += 1
        return ans