# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good_nodes = 0
        curr = root


        def dfs(node,maxSoFar):

            nonlocal good_nodes
            
            if not node:
                return 

            if node.val >= maxSoFar:
                good_nodes += 1

            new_max = max(maxSoFar,node.val)

            dfs(node.left,new_max)
            dfs(node.right,new_max)
            
        dfs(root,root.val)

        return good_nodes

