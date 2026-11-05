class Solution:
    def mySqrt(self, x: int) -> int:
        result = 0 
        left = 0  
        right = x 

        while left <= right:

            mid = left + (right-left) //2 
            # if mid **2 <= x
            if mid * mid <= x:
                result = mid
                left = mid + 1 
            else:
                right = mid - 1
            
        return result

        