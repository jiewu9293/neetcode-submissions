class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res,l,r = 0, 0, len(heights) -1
        while l < r:
            area = min(heights[l],heights[r]) * (r-l)
            res = max(area,res)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res