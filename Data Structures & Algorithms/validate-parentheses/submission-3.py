class Solution:
    def isValid(self, s: str) -> bool:
        # replace  O(n) whileO(n)
        # s O(n) 
        while '()' in s or '[]'in s or '{}' in s:
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')
        return s == ""