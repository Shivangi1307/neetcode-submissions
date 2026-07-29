from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        count = Counter(t)
        need = {ch:0 for ch in t}
        res = []

        for right in range(len(s)):
            
            if s[right] in t or s[left] in t:
                
                if s[right] in t:
                    count[s[right]] -= 1

                while count[s[left]] < 0 or s[left] not in t:
                    if count[s[left]] < 0:
                        count[s[left]] += 1

                    left += 1
                
            else:
                left += 1

            if count <= Counter():
                res.append(s[left:right+1])
                count[s[left]] += 1
                left += 1

        print(res)
        return "" if not res else min(res,key = len) 

            


