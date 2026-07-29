import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort()
        res = []
        length = {}

        for query in queries:
            length[query] = []
            for start,end in intervals:

                if start > query:
                    break
                
                if start <= query <= end:
                    duration = end - start + 1
                    heapq.heappush(length[query],(duration,[start,end]))
            
            
            if not length[query]:
                heapq.heappush(length[query],(-1,[None,None]))

        for key in queries:
            res.append(length[key][0][0])

        return res