class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # create a hasmap to count the frequency of letters from s with the given order
        counts = {}
        # create the output list
        output = []
        for ch in s:
            if ch in order:
                counts[ch] = counts.get(ch, 0) + 1
            else:
                output.append(ch)
        
        for ch in order:
            output = output + [ch * counts.get(ch, 0)]
        
        return ''.join(output)
            