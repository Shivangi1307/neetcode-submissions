class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        wrd = ""
        i = 0
        j = 0
        
        while i < len(word1) and j < len(word2):
            wrd += word1[i]
            wrd += word2[j]

            i += 1
            j += 1

        while i < len(word1):
            wrd += word1[i]
            i += 1
        
        while j < len(word2):
            wrd += word2[j]
            j += 1


        return wrd
