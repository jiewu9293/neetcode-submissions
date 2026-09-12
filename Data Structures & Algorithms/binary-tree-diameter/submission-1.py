# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
diameter = num of edges of the longest path between any two nodes within the tree
for each node diameter
height left subtree + height of right subtree

"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def height(node):
            nonlocal diameter
            if node is None:
                return 0 
            left_height = height(node.left)
            right_height = height(node.right)
            #At each node,  calculate the longest path passing through the current node
            diameter = max(diameter, left_height+right_height)
            #return height of substree
            return 1 + max(left_height,right_height)
        height(root)
        return diameter