# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#for both values are smaller than the current node -> both must lie in the left subtree.
#If both values are greater than the current node -> both must lie in the right subtree
# the current node is the split point where one node is on the left and the other is on the right (or one is equal to the current node).
#That split point is the Lowest Common Ancestor (LCA).
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root
        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                return current
                
            
            