#DIJIKSTRA AKLGO -- weighted

import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        rows = len(heights)
        cols = len(heights[0])

        efforts = [[float("inf")] * cols for _ in range(rows)]
        efforts[0][0] = 0

        heap = [(0,0,0)]

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:

            currEffort,r,c = heapq.heappop(heap)

            if currEffort > efforts[r][c]:
                continue

            if r == rows - 1 and c == cols - 1:
                return currEffort

            for dr,dc in directions:
                
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue

                diff = abs(heights[nr][nc] - heights[r][c])
                newEffort = max(diff,currEffort)

                if newEffort < efforts[nr][nc]:

                    efforts[nr][nc] = newEffort
                    heapq.heappush(heap,(newEffort,nr,nc))


        return 0