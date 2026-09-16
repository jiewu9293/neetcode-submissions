# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
前序遍历 + 空节点标记。
For each non-null node, I append its value to a list
For a null child, I append a special marker such as "#". The null markers are necessary because preorder values alone cannot uniquely represent the structure of a binary tree

"""
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        values = []
        def dfs(node):
            if node is None:
                values.append("N")
                return
            #preorder
            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(values)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = iter(data.split(","))
        def dfs():
            value = next(values)

            if value == "N":
                return None
            
            node = TreeNode(int(value))
            node.left = dfs()
            node.right = dfs()
            
            return node
        return dfs()
