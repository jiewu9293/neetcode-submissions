class Solution:
    """
    return all possible combinations of k
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        #current combination
        path = []
        def backtrack(start: int) -> None:
             # A valid combination has been constructed
            if len(path) == k:
                result.append(path.copy())
                return

            # Number of elements still needed    
            remaining = k - len(path)
            #largest number we can choose
            max_start = n - remaining + 1
            for num in range(start,max_start + 1):
                path.append(num)
                backtrack(num+1)
                path.pop()
        backtrack(1)
        return result