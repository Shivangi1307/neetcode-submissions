class Solution:
    def rob(self, nums: List[int]) -> int:
    

        one,two = 0,0

        for money in nums:
            curr = max(two,one + money)

            one = two
            two = curr

        return two  