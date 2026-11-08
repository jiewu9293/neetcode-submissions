# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        stack = [root]
        pre = None
        while stack:
            cur = stack[-1]
            is_leaf = cur.left is None and cur.right is None
            children_finished = (
                pre is not None
                and (pre is cur.left or pre is cur.right)
            )
            if is_leaf or children_finished:
                result.append(cur.val)
                stack.pop()
                pre = cur
            
            else:
                if cur.right is not None:
                    stack.append(cur.right)
                if cur.left is not None:
                    stack.append(cur.left)
        return result