# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # [2,3]
        # [4,5,6]
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_len = len(queue)
            level_nodes = []
            for _ in range(level_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                level_nodes.append(node.val)
            
            result.append(level_nodes.pop())

        return result


