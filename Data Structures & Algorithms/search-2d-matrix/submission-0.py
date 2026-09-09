class Solution:
    #把二维矩阵想象成一个有序的一维数组，然后进行一次二分搜索。
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        left = 0
        right = rows * columns - 1

        while left <= right:
            mid = (left + right)   //2 

            row = mid // columns
            
            column = mid % columns

            value = matrix[row][column]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1 
        return False
        