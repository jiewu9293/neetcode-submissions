class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #convert input to set initialise variable
        # for each elem do check num -1 not in set ( check num is starting)

        store = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in store:
                streak = 1
                while num + streak in store:
                    streak += 1
                res = max(res,streak)
        return res
