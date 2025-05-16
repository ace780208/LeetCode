class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        # build hashmaps to store the frequency of each letter in word1 and 2
        counts1 = dict()
        counts2 = dict()
        for s in word1:
            counts1[s] = counts1.get(s, 0) + 1
        for s in word2:
            counts2[s] = counts2.get(s, 0) + 1
        
        s1_key = counts1.keys()
        s2_key = counts2.keys()
        if s1_key != s2_key:
            print("key fail")
            return False
        
        s1_freq = sorted(counts1.values())
        s2_freq = sorted(counts2.values())

        if len(s1_freq) != len(s2_freq):
            return False
        for index in range(len(s1_freq)):
            if s1_freq[index] != s2_freq[index]:
                return False

        return True