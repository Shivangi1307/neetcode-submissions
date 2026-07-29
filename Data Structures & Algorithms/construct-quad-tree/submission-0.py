"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def build(r,c,size):

            first = grid[r][c]

            for i in range(r,r+size):
                for j in range(c,c+size):

                    if grid[i][j] != first:

                        size = size // 2

                        return Node(
                            False,
                            False,
                            build(r,c,size),
                            build(r,c+size,size),
                            build(r+size,c,size),
                            build(r+size,c+size,size),
                        ) 
            
            return Node(first == 1,True)

        return build(0,0,len(grid))
        