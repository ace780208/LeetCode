class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counts = dict()
        ans = 0
        for stone in stones:
            if stone in jewels:
                counts[stone] = counts.get(stone, 0) + 1
        
        for jew, count in counts.items():
            ans += count
        return ans