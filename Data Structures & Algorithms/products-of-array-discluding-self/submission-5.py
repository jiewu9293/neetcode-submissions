class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        # [1,2,4,6] [48,24,12,8]
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if j != i:
                    prod *= nums[j]
            res[i] = prod
        return res

            
        
