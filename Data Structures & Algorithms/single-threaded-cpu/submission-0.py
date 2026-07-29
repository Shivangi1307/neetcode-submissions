import heapq
from collections import deque

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        result = []
        heap = []

        tasks = [(enqueueTimei,processingTimei,index) for index,(enqueueTimei,processingTimei) in enumerate(tasks)]    
        tasks.sort()
    
        time = 0
        i = 0
        size = len(tasks)

        while i < size or heap:

            if not heap:
                time = max(time,tasks[i][0])

            
            while i < size and tasks[i][0] <= time:

                enqueueTimei,processingTimei,index = tasks[i]

                heapq.heappush(heap,(processingTimei,index))

                i += 1

            processingTimei,index = heapq.heappop(heap)
            time += processingTimei
            
            result.append(index)
                
        return result
