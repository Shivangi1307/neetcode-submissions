from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = {}

        for i, char in enumerate(s):
            last[char] = i

        ans = []
        start = 0
        end = 0
        for i, char in enumerate(s):

            end = max(end,last[char])

            if i == end:
                ans.append(end - start + 1)
                start = i + 1

        return ans
