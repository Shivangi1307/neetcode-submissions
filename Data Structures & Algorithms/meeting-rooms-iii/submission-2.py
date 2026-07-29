import heapq
from collections import defaultdict 

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()

        available = [i for i in range(n)]
        heapq.heapify(available)

        occupied = []
        count = [0] * n

        for start,end in meetings:

            duration = end - start

            while occupied and occupied[0][0] <= start:
                final_end,room = heapq.heappop(occupied)

                heapq.heappush(available,room)

            if available:
                
                room = heapq.heappop(available)
                heapq.heappush(occupied,(end,room))

            else:
                finish_time,room = heapq.heappop(occupied)

                new_end = finish_time + duration
                heapq.heappush(occupied,(new_end,room))

            count[room] += 1

        return count.index(max(count))
            