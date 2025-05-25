class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counts = Counter(s1)

    
        for left in range(len(s2)):
            if s2[left] in s1_counts:
                s2_counts = Counter(s2[left: left+len(s1)])
                if s1_counts == s2_counts:
                    return True
        
        return False

