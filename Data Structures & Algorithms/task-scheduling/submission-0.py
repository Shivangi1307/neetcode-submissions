import heapq
from collections import deque,Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = Counter(tasks)
        heap = [-count for count in freq.values()]

        heapq.heapify(heap)

        queue = deque()
        time = 0
        
        while queue or heap:

            time += 1

            if heap:

                count = heapq.heappop(heap)
                count += 1

                if count != 0:
                    queue.append((count,time+n))

            if queue and queue[0][1] == time:
                heapq.heappush(heap,queue.popleft()[0])

        return time
            