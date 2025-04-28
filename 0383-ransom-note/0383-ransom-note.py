class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counts = dict()
        mag_counts = dict()
        for txt in ransomNote:
            ransom_counts[txt] = ransom_counts.get(txt, 0) + 1
        for txt in magazine:
            mag_counts[txt] = mag_counts.get(txt, 0) + 1
        
        for txt, count in ransom_counts.items():
            if count > mag_counts.get(txt, 0):
                return False
            
        return True
        