class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,4,6] [-1,0,1,2,3] [0,]
        # no zero 1 zero more than 1 zero
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i,n in enumerate(nums):
            if zero_cnt:
                res[i] = 0 if n else prod 
            else:
                res[i] = prod // n
        return res


        



