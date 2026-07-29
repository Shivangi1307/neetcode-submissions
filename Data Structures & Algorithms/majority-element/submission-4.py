from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        my_dict = Counter(nums)
        sorted_dict = dict(sorted(my_dict.items(), key = lambda x:x[1], reverse = True))
        
        return next(iter(sorted_dict))