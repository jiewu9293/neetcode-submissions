class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #handle edge case if input empty should have no combination
        result = [] 
        #current combination
        path = []
        if not digits:
            return []
        #map each digit to corresponding letters
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
    #index to track which digit we are currently processing
        def backtrack(index: int) -> None:
        #If every digit has been processed,
        # record the current complete combination.
            if index == len(digits):
                result.append("".join(path))
                return
            # Get all possible letters for the current digit.
            letters = phone[digits[index]]
             # Try every possible letter at the current position.
            for letter in letters:

                #make a choice 
                path.append(letter)
                
                backtrack(index+1)
                #undo the choice
                path.pop()
        backtrack(0)
        return result

            