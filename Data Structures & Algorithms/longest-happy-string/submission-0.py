import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        heap = []

        if a:
            heapq.heappush(heap,(-a,'a'))
        
        if b:
            heapq.heappush(heap,(-b,'b'))

        if c:
            heapq.heappush(heap,(-c,'c'))

        
        result = []
        while heap:

            count1,ch1 = heapq.heappop(heap)

            if len(result) >= 2 and result[-1] == ch1 and result[-2] == ch1:

                if not heap:
                    break

                count2,ch2 = heapq.heappop(heap)
                result.append(ch2)
                count2 += 1

                if count2 < 0:
                    heapq.heappush(heap,(count2,ch2))

                heapq.heappush(heap,(count1,ch1))

            else:
                result.append(ch1)
                count1 += 1

                if count1 < 0:
                    heapq.heappush(heap,(count1,ch1))


        return "".join(result)                


        
        