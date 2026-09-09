class Solution:
    """
    left = 1 (minimum possible speed)
right = max(piles) (maximum needed speed)

    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Set the search range:
        left = 1
        right = max(piles)

        while left < right:
            #(left + right) // 2  Let mid be the current speed to test.
            # Compute the total hours needed using this speed.
            speed = left + (right - left) //2 

            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            #If the total hours is within the allowed time h:
            #This speed works, so record it.
            #If the total hours is within the allowed time h
            # Try to find a smaller working speed by searching the left half.

            #Speed is too slow, so search in the right half.
            #After the search ends, return the smallest valid speed found.
            if hours <= h:
                right = speed
            else:
                left = speed + 1 
            
        return left

            


        