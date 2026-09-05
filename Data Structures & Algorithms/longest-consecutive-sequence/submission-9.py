class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 

        nums.sort()
        #initialise
        longest = 1 # length of the longest sequence so far
        current = 1 # length of current sequence
        #start from 2nd elem
        for i in range(1, len(nums)):
            #if duplicate skip to next num
            if nums[i] == nums[i - 1]:
                continue
            # if consecutive update current
            if nums[i] == nums[i - 1] + 1:
                current += 1
            else:
            #reset to 1 
                current = 1
            # update longest
            longest = max(longest,current)
        return longest
