# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        lHeight = self.heightHelper(0, root.left)
        rHeight = self.heightHelper(0, root.right)
        if abs(lHeight-rHeight) <= 1 and lHeight != 1001 and rHeight != 1001:
            return True
        return False
    
    def heightHelper(self, height : int, root: Optional[TreeNode]) -> int:
        if root is None:
            return height
        lHeight = self.heightHelper(height+1, root.left)
        rHeight = self.heightHelper(height+1, root.right)
        if abs(lHeight-rHeight) <= 1:
            return max(lHeight, rHeight)
        else:
            return 1001