class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k+1):

            temp = prices.copy()

            for u,v,cost in flights:

                if prices[u] == float("inf"):
                    continue

                if cost + prices[u] < temp[v]:
                    temp[v] = cost + prices[u]


            prices = temp

        return prices[dst] if prices[dst] != float("inf")  else -1 
