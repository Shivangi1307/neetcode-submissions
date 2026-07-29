class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 0 
        i = 0

        for i in range(len(s)):
            sub_str = ""
            while i < len(s) and  s[i] not in sub_str:
                sub_str += s[i] 
                i += 1
            max_length = max(max_length,len(sub_str))

        
        return max_length

            