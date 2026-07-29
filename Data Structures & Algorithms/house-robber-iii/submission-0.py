# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):

            if not node:
                return (0,0)

            leftRob, leftNotRob = dfs(node.left)
            rightRob, rightNotRob = dfs(node.right)


            rob = node.val + leftNotRob + rightNotRob
            notrob = max(leftNotRob,leftRob) + max(rightNotRob,rightRob)

            return (rob,notrob)

        rob,notrob = dfs(root)

        return max(rob,notrob)