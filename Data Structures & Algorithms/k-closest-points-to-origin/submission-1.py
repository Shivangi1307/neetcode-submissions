import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        result = []
        heap = []

        for x,y in points:
            dist = x*x + y*y
            heap.append([dist,x,y])

        heapq.heapify(heap)

        for _ in range(k):
            _,y,z = heapq.heappop(heap)
            result.append([y,z])

        return result