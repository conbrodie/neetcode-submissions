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
        self.diameter = max(self.diameter, left + right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.diameter = 0
        self.height(root)
        return self.diameter