# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(l,r):
            if type(l)==TreeNode and type(r)==TreeNode and l.val == r.val:
                return helper(l.right,r.left) and helper(l.left,r.right)
            else:
                return l == r
        return helper(root.left,root.right) 

