class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counts = {}
        for key in s1:
            s1_counts[key] = s1_counts.get(key, 0) + 1

    
        for left in range(len(s2) - len(s1)+1):
            if s2[left] not in s1_counts:
                continue
            s2_counts = {}
            for right in range(len(s1)):
                s2_counts[s2[left+right]] = s2_counts.get(s2[left+right], 0) + 1

            if s1_counts == s2_counts:
                return True
        
        return False

