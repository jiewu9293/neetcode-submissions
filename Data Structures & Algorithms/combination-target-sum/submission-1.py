class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #enable pruning
        nums.sort()
        result = []
        path = []
        #starting from index
        #searches for all valid combinations that sum to remain
        def dfs(start: int, remain: int) -> None:
            # A valid combination has been found
            if remain == 0:
                result.append(path.copy())
                return

            for i in range(start, len(nums)):
                value = nums[i]
                #all later values too large
                if value > remain:
                    break
                #choose the value
                path.append(value)
                #move to the next level
                #Passing i allows the next recursive call to choose the same candidate again.
                dfs(i,remain - value)
                #undo the choice
                path.pop()
        dfs(0,target)
        return result
