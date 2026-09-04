class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        glomax,glomin,curmax,curmin,total = float("-inf"),float("inf"),0,0,0

        for num in nums:
            curmax = max(curmax+num,num)
            curmin = min(curmin+num,num)
            total += num
            glomax = max(glomax,curmax)
            glomin = min(glomin,curmin)
        
        return max(glomax,total-glomin) if glomax > 0 else glomax