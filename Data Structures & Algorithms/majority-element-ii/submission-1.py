from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        my_dict = Counter(nums)
        sorted_dict = dict(sorted(my_dict.items(),key = lambda x: x[1], reverse = True))

        res = []
        for key in sorted_dict:
            print(sorted_dict[key])
            if sorted_dict[key] > len(nums)//3:
                res.append(key)

        return res
        # return sorted(nums)