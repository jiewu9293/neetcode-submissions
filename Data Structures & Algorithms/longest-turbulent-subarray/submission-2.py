class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        #length of the turbulant subarray ending with increasing comparision
        up = 1
        #length of the turbulant subarray ending with decreasing comparision
        down = 1
        #global maximum length
        answer = 1

        for i in range(1, len(arr)):
            #right now increasing before must be decreasing
            if arr[i] > arr[i - 1]:
                up = down + 1
                down = 1
            elif arr[i] < arr[i - 1]:
                # A decreasing step must follow an increasing step
                down = up + 1
                up = 1
            else:# the turbulant pattern is broken
                up = 1
                down = 1
            answer = max(up,down,answer)
        return answer
