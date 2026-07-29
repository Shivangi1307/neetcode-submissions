from typing import List

class Solution:
    
    def merge(self, nums, left, mid, right):
        temp = []
        i, j = left, mid + 1

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= right:
            temp.append(nums[j])
            j += 1

        for k in range(len(temp)):
            nums[left + k] = temp[k]

    def mergesort(self, nums, left, right):
        if left >= right:
            return

        mid = (left + right) // 2
        self.mergesort(nums, left, mid)
        self.mergesort(nums, mid + 1, right)

        self.merge(nums, left, mid, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums, 0, len(nums) - 1)
        return nums