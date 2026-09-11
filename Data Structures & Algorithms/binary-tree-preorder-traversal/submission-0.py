# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#处理当前节点 → 递归左子树 → 递归右子树

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if node is None:
                return
            
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result


        
