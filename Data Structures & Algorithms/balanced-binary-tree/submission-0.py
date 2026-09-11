# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
判断一棵树是否平衡，需要知道两件事：
1. 左子树是否平衡；
2. 右子树是否平衡；
3. 左右子树的高度差是否不超过 1。
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #return -1 if it's not balance
        #return its height if it's balanced
        def get_height(node):
            if node is None:
                return 0
            left_height = get_height(node.left)
            #any subtree inbalanced tree is inbalanced
            if left_height == -1:
                return -1 
            right_height = get_height(node.right)

            if right_height == -1:
                return -1 
            #check if tree is balanced
            if abs(left_height - right_height) > 1:
                return -1
            #calculate tree height
            return max(left_height, right_height) + 1

        return get_height(root) != -1
            
            
