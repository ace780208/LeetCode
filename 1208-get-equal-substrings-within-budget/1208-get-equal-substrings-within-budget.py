class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        ans = 0
        cost = 0
        for right in range(len(s)):
            right_diff = abs(ord(s[right]) - ord(t[right]))
            cost += right_diff
            while(cost > maxCost):
                left_diff = abs(ord(s[left]) - ord(t[left]))
                cost -= left
                left += 1
            ans = max(ans, right - left + 1)
        return ans