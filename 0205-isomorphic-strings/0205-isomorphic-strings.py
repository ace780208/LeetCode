class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pair = {}
        for index in range(len(s)):
            if s[index] in pair:
                if pair[s[index]] != t[index]:
                    return False
            else:
                pair[s[index]] = t[index]

        return True
        