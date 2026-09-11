# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
The depth of a tree = 1 + maximum depth of its left and right subtrees.
If a node is None, its depth is 0.
如果当前节点不存在，说明这棵子树是空树。
空树没有任何节点，因此深度是 0
取左右子树中更深的一边，再加上当前节点这一层
# If root exists with no children, depth is 1 (one node)
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1