# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def fun(root, s, targetSum):
            if not root:
                return False
            s+=root.val
            if not root.left and not root.right:
                return s == targetSum
            return fun(root.left,s, targetSum) or fun(root.right,s, targetSum)
        return fun(root,0,targetSum)
        
