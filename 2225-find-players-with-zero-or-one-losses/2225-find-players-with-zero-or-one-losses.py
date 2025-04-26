from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        counts = defaultdict(int)
        for match in matches:
            counts[match[0]] += 0
            counts[match[1]] += 1
            
        no_lost = []
        one_lost = []
        
        for player in counts.keys():
            if counts[player] == 0:
                no_lost.append(player)
            elif counts[player] == 1:
                one_lost.append(player)
        
        return[sorted(no_lost), sorted(one_lost)]