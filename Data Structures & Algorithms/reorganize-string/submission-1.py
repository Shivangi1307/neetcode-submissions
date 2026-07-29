from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        freq = Counter(s)

        heap = [(-count,ch) for ch,count in freq.items()]
        heapq.heapify(heap)

        result = []

        prevFreq = 0
        prevChar = ""

        while heap:

            count,ch = heapq.heappop(heap)
            result.append(ch)
            count += 1

            if prevFreq < 0:
                heapq.heappush(heap,(prevFreq,prevChar))

            prevFreq = count
            prevChar = ch

        if len(result) != len(s):
            return ""

        return "".join(result)


        