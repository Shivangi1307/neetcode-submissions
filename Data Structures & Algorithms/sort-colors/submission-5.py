class Solution:

    def sortColors(self, nums: List[int]) -> None:
        
        bucket = [[], [], []]

        for num in nums:
            bucket[num].append(num)
        
        index = 0
        for b in bucket:
            for num in b:
                nums[index] = num
                index += 1