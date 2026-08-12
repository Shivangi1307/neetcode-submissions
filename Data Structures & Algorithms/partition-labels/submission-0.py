from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        count = Counter(s)
        answer = []

        left = 0
        length = 0
        for right in range(len(s)):

            count[s[right]] -= 1

            while left < len(s) and count[s[left]] == 0:
                left += 1
                length += 1

            if left > right:
                answer.append(length)
                length = 0

        return answer
