class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        #water trapped  = min(leftmax,rightmax) - currheight
        #shorter side decides
        res = 0
        l ,r = 0 , len(height) -1 
        leftmax,rightmax = height[l],height[r]
        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(height[l],leftmax)
                res += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(height[r],rightmax)
                res += rightmax - height[r]
        return res

