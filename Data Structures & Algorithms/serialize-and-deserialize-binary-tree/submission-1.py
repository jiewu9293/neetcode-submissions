# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
N represent empty node
dfs with preorder traversal
node val added to list
list join to a string
"""
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        values = []
        def dfs(node):
            if node is None:
                values.append("N")
                return
            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(values)
#N means empty node
#create a node with nodeval
# split string to a list
#create a iterator with the list
#process each elem in the iterator


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #split a string to a list and create a iterator
        values = iter(data.split(",") )
        def dfs():
            value = next(values)

            if value == "N":
                return None
            node = TreeNode(int(value))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


