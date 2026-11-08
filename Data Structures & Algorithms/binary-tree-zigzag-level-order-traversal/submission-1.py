# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            current_level = []
            level_size = len(queue)

            for _ in range(level_size):
                if left_to_right:
                    node = queue.popleft()
                    
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
                else:
                    node = queue.pop()

                    if node.right is not None:
                        queue.appendleft(node.right)
                    if node.left is not None:
                        queue.appendleft(node.left)
                current_level.append(node.val)
            result.append(current_level)
            left_to_right = not left_to_right
        return result

                    

                    


            