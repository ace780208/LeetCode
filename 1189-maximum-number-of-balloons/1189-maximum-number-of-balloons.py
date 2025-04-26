class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = dict()
        for txt in text:
            if txt in 'balon':
                counts[txt] = counts.get(txt, 0) + 1
        ans = len(text)//7
        for txt in 'balon':
            if txt == 'l' or txt == 'o':
                ans = min(ans, counts.get(txt, 0)//2)
            else:
                ans = min(ans, counts.get(txt, 0))
        return ans
        