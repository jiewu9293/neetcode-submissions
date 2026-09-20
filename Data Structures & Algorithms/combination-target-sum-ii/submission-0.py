class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #skip duplicate at same level recursion
        """
        The backtracking function takes a start index and a remaining target. At each recursion level, I iterate through the candidates starting from start.
        """
        path = []
        result = []
        candidates.sort()
        def backtrack(start,remain):
            #if valid combination is found 
            if remain == 0:
                return result.append(path.copy())
            
            #iterate every candidate from start
            for i in range(start,len(candidates)):
                current = candidates[i]

                #skip duplicate at same recursion level
                if candidates[i-1] == current and i > start:
                    continue
                #stop early if later values too large
                if current > remain:
                    break
                
                #make a choice
                path.append(current)
                #move to the next level
                backtrack(i+1,remain-current)
                #undo the choice
                path.pop()
        backtrack(0,target)
        return result
                

            
            
