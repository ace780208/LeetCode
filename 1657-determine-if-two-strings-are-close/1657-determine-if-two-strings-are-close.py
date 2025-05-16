class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # build hashmaps to store the frequency of each letter in word1 and 2
        counts1 = dict()
        counts2 = dict()
        for s in word1:
            counts1[s] = counts1.get(s, 0) + 1
        for s in word2:
            counts2[s] = counts2.get(s, 0) + 1
        
        s1_key = sorted(counts1.keys())
        s2_key = sorted(counts2.keys())

        if len(s1_key) != len(s2_key):
            return False
        for index in range(len(s1_key)):
            if s1_key[index] != s2_key[index]:
                return False
        
        s1_freq = sorted(counts1.values())
        s2_freq = sorted(counts2.values())

        if len(s1_freq) != len(s2_freq):
            return False
        for index in range(len(s1_freq)):
            if s1_freq[index] != s2_freq[index]:
                return False
        
        return True