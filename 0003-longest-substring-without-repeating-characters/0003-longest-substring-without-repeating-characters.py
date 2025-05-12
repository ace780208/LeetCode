class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_index = {}
        left = 0
        ans = 0
        for right in range(len(s)):
            if s[right] in letter_index:
                left = max(left, letter_index[s[right]])
            ans = max(ans, right - left + 1)
            letter_index[s[right]] = right + 1
        return ans