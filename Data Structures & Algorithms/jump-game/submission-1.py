class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #farthest index we can reach
        farthest = 0
        for i, jump_length in enumerate(nums):
            ## If the current index is beyond farthest,
            # we cannot reach this position.
            if i > farthest:
                return False

            farthest = max(farthest, i + jump_length)

            # If we can reach or pass the last index, return early.
            if farthest >= len(nums) -1:
                return True
        

