# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        # diameter of sub-tree
        diameter = left_height + right_height
        self.best = max(self.best, diameter)

        return 1 + max(left_height, right_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        self.get_height(root) 
        return self.best
        

        