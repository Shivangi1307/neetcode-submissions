class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow1 = nums[0]
        fast = nums[0]

        while True:

            slow1 = nums[slow1]
            fast = nums[nums[fast]] 

            if fast == slow1:
                break
        
        slow2 = nums[0]

        while slow1 != slow2:
            slow1 = nums[slow1]
            slow2 = nums[slow2]

        return slow1