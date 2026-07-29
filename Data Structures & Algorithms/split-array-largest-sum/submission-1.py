class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:

            med = left + ( right - left ) // 2

            lrg_sum = 0
            subarrs = 1
            for num in nums:
                if lrg_sum + num <= med:
                    lrg_sum += num
                else:
                    subarrs += 1
                    lrg_sum = num

            if subarrs > k:
                left = med + 1
            else:
                right = med

        return left