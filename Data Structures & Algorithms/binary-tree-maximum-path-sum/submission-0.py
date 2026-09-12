# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = float("-inf")
        #return the maximum path sum starting from node
        def dfs(node):
            nonlocal answer
            #if subtree empty return 0 contribution
            if node is None:
                return 0
            #clamp negative subtree contribution to zero
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            #calculate current path sum and try to update global answer
            answer = max(answer, left + node.val + right)
            #return contribution to parent
            #can only use one branh
            return node.val + max(left, right)

        dfs(root)
        return answer
