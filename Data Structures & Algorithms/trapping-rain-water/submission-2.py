class Solution:
    def trap(self, height: List[int]) -> int:
        #check input 
        if not height:
            return 0
        #initialise stack
        #initialise res
        stack = []
        res =0
        #h = min(left, right) - mid
        #w = i - stack[-1] - 1
        #stack stores the index of the height
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    h = min(left,right) - mid
                    w = i - stack[-1] - 1
                    res += h * w 
            stack.append(i)
        return res
