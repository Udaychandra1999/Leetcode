# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        res =[]
        if root is None:
            return []
        queue.append(root)
        while len(queue) > 0:
            level =[]
            for _ in range(len(queue)):
                x = queue.pop(0)
                level.append(x.val)
                if x.left is not None:
                    queue.append(x.left)
                if x.right is not None:
                    queue.append(x.right)
            res.append(level)
        return res 