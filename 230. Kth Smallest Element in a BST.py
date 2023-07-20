# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: 
        def bfs(root):
            if not root : return []
            result = [root.val]
            left_vals = bfs(root.left)
            right_vals = bfs(root.right)
            result.extend(left_vals)
            result.extend(right_vals)
            return result
        l = sorted(bfs(root))
        return l[k-1]
