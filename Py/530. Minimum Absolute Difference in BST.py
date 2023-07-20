# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        L = []
        minDiff = 999999
        def inorder(root):
            if root:
                inorder(root.left)
                L.append(root.val)
                inorder(root.right)
        inorder(root)
        
        for i in range(len(L) - 1):
            minDiff = min(minDiff, abs(L[i] - L[i+1]))
        
        return minDiff

        
