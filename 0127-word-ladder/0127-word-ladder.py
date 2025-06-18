from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordlen = len(beginWord)
        def jump(a, b):
            diff = 0
            for i in range(wordlen):
                if a[i] != b[i]:
                    diff += 1
                
                if diff > 1:
                    break
            
            return True if diff == 1 else False
        
        no_jump = True
        graph = dict()
        graph[beginWord] = []
        for i in range(len(wordList)):
            if jump(beginWord, wordList[i]):
                no_jump = False
                graph[beginWord].append(wordList[i])
        if no_jump:
            return 0
        
        listlen = len(wordList)
        for i in range(listlen):
            if wordList[i] not in graph:
                graph[wordList[i]] = []
            for j in range(i+1, listlen):
                if wordList[j] not in graph:
                    graph[wordList[j]] = []
                if jump(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        
        queue = deque([(beginWord, 1)])
        seen = set()
        seen.add(beginWord)
        while queue:
            node, jump_time = queue.popleft()
            if node == endWord:
                return jump_time
            for next_jump in graph[node]:
                if next_jump not in seen:
                    seen.add(next_jump)
                    queue.append((next_jump, jump_time + 1))
        
        return 0
            
                