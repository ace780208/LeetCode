class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = Counter(s1)
        n = len(s1)
        for left in range(len(s2)):
            if s2[left] in s1_counts:
                s2_counts = Counter(s2[left: left+n])
                if s1_counts == s2_counts:
                    return True
        
        return False

