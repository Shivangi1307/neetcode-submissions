class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows = len(board)
        cols = len(board[0])

        visited = set()

        def dfs(r,c,visited):

            visited.add((r,c))

            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            for dr,dc in directions:

                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr,nc) in visited or board[nr][nc] != "O":
                    continue

                dfs(nr,nc,visited)


        for r in range(rows):
            if board[r][0] == "O":
                dfs(r,0,visited)

        for r in range(rows):
            if board[r][cols-1] == "O":
                dfs(r,cols-1,visited)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c,visited)

        for c in range(cols):
            if board[rows-1][c] == "O":
                dfs(rows-1,c,visited)


        for r in range(rows):
            for c in range(cols):

                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"
        