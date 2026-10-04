# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left = self.height(node.left)
        right = self.height(node.right)
        diameter = left + right

        self.best = max(self.best, diameter) 

        return 1 + max(left, right)

        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        self.height(root) 
        return self.best
