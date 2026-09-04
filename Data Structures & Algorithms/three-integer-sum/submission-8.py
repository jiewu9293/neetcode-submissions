class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # fix a number reduce 3 sum to 2 sum
        #remove duplicate in outloop and inner loop
        nums.sort()
        res = []
        for i in range(len(nums)):
            l,r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                if total < 0:
                    l += 1
                if total >0:
                    r -= 1
        return res
                


            