class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #check num -1 not in set
        store = set(nums)
        res = 0
        for num in store:
            if num-1 not in store:
                length = 1
                while num + length in store:
                    length += 1
                res = max(res,length)
        return res