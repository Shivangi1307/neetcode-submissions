class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])

        atlantic = set()
        pacific = set()

        def dfs(r,c,visited):

            visited.add((r,c))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr,dc in directions:

                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr,nc) in visited or heights[nr][nc] < heights[r][c]:
                    continue

                dfs(nr,nc,visited)


        # Top
        for c in range(cols):
            dfs(0,c,pacific)

        # Left
        for r in range(rows):
            dfs(r,0,pacific)

        # Bottom
        for c in range(cols):
            dfs(rows-1,c,atlantic)
        
        # Right
        for r in range(rows):
            dfs(r,cols-1,atlantic)


        ans = []

        for r in range(rows):
            for c in range(cols):

                if (r,c) in atlantic and (r,c) in pacific:
                    ans.append([r,c])

        return ans