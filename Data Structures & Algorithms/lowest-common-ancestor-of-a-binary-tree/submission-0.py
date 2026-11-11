# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return None
            if node is p or node is q:
                return node
            left_result = dfs(node.left)
            right_result = dfs(node.right)

            if left_result is not None and right_result is not None:
                return node
            if left_result is not None:
                return left_result
            return right_result


            

        return dfs(root)  
        