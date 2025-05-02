class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        curr = 0
        for right in range(len(s)):
            if self.isVowel(s[right]):
                curr += 1
            while((right - left + 1) > k):
                if self.isVowel(s[left]):
                    curr -= 1
                left += 1
            ans = max(ans, curr)
        
        return ans

    def isVowel(self, s: str) -> bool:
        return s in ["a", "e", "i", "o", "u"]