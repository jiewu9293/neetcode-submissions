class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        result = 0

        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid <= x:
                result = mid    # 记录目前找到的最大可行值
                left = mid + 1  # 尝试找更大的值
            else:
                right = mid - 1

        return result