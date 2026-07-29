import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        passangers = 0
        heap = []

        trips.sort(key = lambda x:x[1])

        for numPassanger,start,end in trips:

            while heap and heap[0][0] <= start:
                dropoff,people = heapq.heappop(heap)
                passangers -= people

            passangers += numPassanger

            if passangers > capacity:
                return False

            heapq.heappush(heap,(end,numPassanger))


        return True
        
