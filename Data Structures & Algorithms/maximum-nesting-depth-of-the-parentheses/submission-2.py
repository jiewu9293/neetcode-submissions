class Solution:
    def maxDepth(self, s: str) -> int:
        #current paren depth
        depth = 0
        max_depth = 0
        for char in s:
            #enter new depth
            if char == "(":
                depth += 1
                max_depth = max(max_depth, depth)
            #leave cur level
            elif char == ")":
                depth -= 1
        return max_depth
