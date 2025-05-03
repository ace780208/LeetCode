class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pair = {}
        seen = set()
        for index in range(len(s)):
            if s[index] in pair:
                if pair[s[index]] != t[index]:
                    return False
            else:
                if t[index] in seen:
                    return False
                pair[s[index]] = t[index]
                seen.add(t[index])
        return True
