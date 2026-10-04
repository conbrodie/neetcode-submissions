# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node) -> Optional[TreeNode]:
            if not node:
                return [None,0]
            
            left = dfs(node.left)
            right = dfs(node.right)

            return [node, 1 + max(left[1], right[1])]

        n = dfs(root)

        return n[1]          
