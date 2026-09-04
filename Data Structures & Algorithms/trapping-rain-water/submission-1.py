class Solution:
    def trap(self, height: List[int]) -> int:
        #[0,2,0,3,1,0,1,3,2,1]
        #check input
        #intialise leftmax, rightmax list
        n = len(height)
        if not height:
            return 0
        leftMax = [0] * n
        rightMax = [0] * n
        leftMax[0] = height[0]
        for i in range(1,n):
            leftMax[i] = max(height[i],leftMax[i-1])

        rightMax[n-1] = height[n -1 ]
        for i in range(n-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],height[i])
        res = 0 
        for i in range(n):
            res += min(rightMax[i],leftMax[i]) - height[i]
        return res




