from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = Counter(nums)
        result = [] * k

        sorted_dict = dict(sorted(my_dict.items(), key = lambda x : x[1], reverse = True))
       
        for i,key in enumerate(sorted_dict):
            if i == k:
                break
            result.append(key)
            
        return result