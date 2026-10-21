# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root is None):
            return 0
        return max(self.DepthHelper(1, root.left), self.DepthHelper(1, root.right))

    def DepthHelper(self, depth: int, root: Optional[TreeNode]) -> int:
        if(root is None):
            return depth
        return max(self.DepthHelper(depth + 1, root.left), self.DepthHelper(depth + 1, root.right))