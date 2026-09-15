# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node,lower, upper):
            if node is None:
                return True
            #validate current node is bst
            if not lower<node.val<upper:
                return False

            return(
                #validate leftsubtree is a bst
                validate(node.left,lower,node.val)
                #validate rightsubtree is a bst
                and validate(node.right,node.val,upper)
            )
            #start validate from rootnode initialise range
        return validate(root,float('-inf'),float('inf'))


        