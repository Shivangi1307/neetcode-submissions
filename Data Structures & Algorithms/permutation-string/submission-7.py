from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = {}
        left = 0

        for right in range(len(s2)):
             
            r_ch = s2[right]
            window[r_ch] = window.get(r_ch,0) + 1

            if right - left + 1 > len(s1):
                l_ch = s2[left]
                window[l_ch] -= 1
                if window[l_ch] == 0:
                    del window[l_ch]
                left += 1

            if window == need:
                return True


        return False

            
