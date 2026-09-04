class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #[2, 3, 4, 4, 4, 10, 20]
        #check empty input 
        #sort input 
        #Initialise variable
        #for each elem if curr != nums[i] curr = nums[i] streak = 0
        # ship the repetitive 
        #update variable
        if not nums:
            return 0 
        nums.sort()
        curr,streak,i,res = nums[0],0,0,0
        while i < len(nums):
            if nums[i] != curr:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            curr += 1
            streak += 1
            res = max(res,streak)
        return res





        