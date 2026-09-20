class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #for edge case if input is empty should have no combination
        if not digits:
            return []
        result = []
        #current combination
        path = []
        phone = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        def backtrack(index):
            #if all digit has been processed
            if len(digits) == index:
                result.append("".join(path))
                return
            #all letter for current digit
            letters = phone[digits[index]]

            for letter in letters:
                #make a choice
                path.append(letter)
                #process the next digit
                backtrack(index+1)
                #undo the choice
                path.pop()
        backtrack(0)
        return result

        