class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # find the index of ch in word
        left = 0
        right = 0
        output = list(word)
        for i in range(len(word)):
            if word[i] == ch:
                right = i
                break
        # use two pointers to reverse the character from left to right
        while left < right:
            output[left], output[right] = output[right], output[left]
            left += 1
            right -= 1

        return ''.join(output)
        
