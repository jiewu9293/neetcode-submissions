class Solution:
    def trap(self, height: List[int]) -> int:
        #[0,2,0,3,1,0,1,3,2,1]
        #check input 
        #initialise res
        # area =  min(leftmax,rightmax) - currheight
        if not height:
            return 0
        res = 0 
        for i in range(len(height)):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax,height[j])
            for j in range(i+1,len(height)):
                rightMax = max(rightMax,height[j])
            res += min(leftMax,rightMax) - height[i]

        return res


        