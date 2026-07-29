import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # if not nums:
        #     return None

        # nums = [-num for num in nums]

        # heapq.heapify(nums)

        # for _ in range(k-1):
        #     heapq.heappop(nums)
        

        # return -nums[0]        

        heap = []

        for num in nums:
            heapq.heappush(heap,num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]