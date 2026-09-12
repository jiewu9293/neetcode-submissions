# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            
            if node1.val != node2.val:
                return False
            return (same_tree(node1.left,node2.left)
            and same_tree(node1.right,node2.right)
             )
        #empty tree always subtree
        if subRoot is None:
            return True
        if root is None:
            return False

        if same_tree(root,subRoot):
            return True
        
        return(
            self.isSubtree(root.left,subRoot)or
            self.isSubtree(root.right,subRoot)
        )
        
        