# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        stack = []
        current = root
        while current is not None or stack:
            if current is not None:
                stack.append(current)

                current = current.left
            else:
                current_node = stack.pop()

                result.append(current_node.val)

                current = current_node.right
        return result
            

            