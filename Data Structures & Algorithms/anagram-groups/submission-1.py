from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      
        group_dict = defaultdict(list)
        
        for word in strs:
            
            freq = [0] * 26
            
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
                
            key = tuple(freq)
            group_dict[key].append(word)
            
        return list(group_dict.values())