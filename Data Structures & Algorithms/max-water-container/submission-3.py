class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        result = 0
        right = len(heights) - 1

        while left < right:
            width = right - left

            container_height = min(heights[left], heights[right])

            area = width * container_height
            result = max(area,result)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1 
        return result