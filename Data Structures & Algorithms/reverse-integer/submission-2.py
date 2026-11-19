class Solution:
    def reverse(self, x: int) -> int:
        """
        x % 10 gets the last digit
        x // 10 removes the last digit
        we add the digit to the result with result = result * 10 + digit    
        ans × 10 + digit > limit
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        limit = 2**31 - 1 if sign == 1 else 2**31
        ans = 0
        while x > 0:
            digit = x % 10
            x //= 10
            #when integer overflow
            if ans > (limit-digit) //10:
                return 0

            ans = ans * 10 + digit
        return sign * ans