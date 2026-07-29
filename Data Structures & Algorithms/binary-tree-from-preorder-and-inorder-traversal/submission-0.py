# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorderMap = {}

        for i, val in enumerate(inorder):
            inorderMap[val] = i

        preindex = 0
        
        def build(left,right):

            nonlocal preindex

            if left > right:
                return None

            rootval = preorder[preindex]
            preindex += 1

            root = TreeNode(rootval)
            mid = inorderMap[rootval]

            root.left = build(left,mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0,len(inorder) - 1)