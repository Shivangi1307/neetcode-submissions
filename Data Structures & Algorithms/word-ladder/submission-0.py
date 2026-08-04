from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        patternMap = defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                patternMap[pattern].append(word)

        queue = deque([(beginWord,1)])
        visited = {beginWord}

        while queue:

            word,length = queue.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):

                pattern = word[:i] + '*' + word[i+1:]

                for neighbour in patternMap[pattern]:

                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour,length+1))

                
                patternMap[pattern] = []

        return 0
        

