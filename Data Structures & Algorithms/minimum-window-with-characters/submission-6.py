from collections import Counter
from math import inf
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        count = Counter(t)
        required = len(t)
        res_len = inf
        res = ""

        for right in range(len(s)):

            if s[right] in count:
                if count[s[right]] > 0:
                    required -= 1

                count[s[right]] -= 1


            while required == 0:

                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res = s[left:right+1]

                if s[left] in t:
                    count[s[left]] += 1
                    if count[s[left]] > 0:
                        required += 1

                left += 1
        
        return res

            


