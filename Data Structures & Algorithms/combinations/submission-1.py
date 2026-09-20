class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        result = []
        #check if valid combination is found
        #recursively call backtrack append the next number to path
        def backtrack(start):
            if len(path) == k:
                result.append(path.copy())
                return
            
            #find num of elem still needed
            remaining = k - len(path)

            #largest num we can choose
            # n-num+1  availble from num to n
            # n-num+1  >= remaining
            # n-remaining +1 >= num
            #pruning 
            max_start = n - remaining + 1
            for num in range(start,max_start+1):
                path.append(num)
                
                backtrack(num+1)
                #undo the choice
                path.pop()
        backtrack(1)
        return result



        