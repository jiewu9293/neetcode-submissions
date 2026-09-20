class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #enable pruning
        nums.sort()
        #store current combination
        path = []
        result = []
        def backtrack(start,remain):

            #if valid combination is found 
            if remain == 0:
                result.append(path.copy())
            #We iterate through the candidates starting from start.
            for i in range(start,len(nums)):
                value = nums[i]
                #all later values too large
                if value > remain:
                    break
                #make a choice
                path.append(value)
                #move to the level
                #allow us to reuse the value
                backtrack(i,remain-value)
                #undo the choice
                path.pop()
        backtrack(0,target)
        return result

                
            
            

        