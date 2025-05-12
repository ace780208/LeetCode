class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pair = {}
        seen = set()
        words = []
        prev_white_index = None
        for index in range(len(s)):
            if s[index] != ' ':
                continue
            tmp_index = index
            if prev_white_index:
                tmp = s[prev_white_index+1: tmp_index]
            else:
                tmp = s[:tmp_index]
            words.append(tmp)
            prev_white_index = tmp_index
        if prev_white_index:
            words.append(s[prev_white_index+1:])
        else:
            words.append(s)

        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in pair:
                if pair[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] in seen:
                    return False
                pair[pattern[i]] = words[i]
                seen.add(words[i])

        return True 