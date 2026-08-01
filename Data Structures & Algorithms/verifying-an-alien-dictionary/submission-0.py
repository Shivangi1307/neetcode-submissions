class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        Alien = {} 
        flag = False

        for i,ch in enumerate(order):
            Alien[ch] = i

        
        for index in range(len(words)-1):

            word1 = words[index]
            word2 = words[index+1]

            for ch1,ch2 in zip(word1,word2):

                if Alien[ch1] > Alien[ch2]:
                    return False

                elif Alien[ch1] < Alien[ch2]:
                    flag = True
                    break

            if not flag and len(word1) > len(word2): return False
        
        return True