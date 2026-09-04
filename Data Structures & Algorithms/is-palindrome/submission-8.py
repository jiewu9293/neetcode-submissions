class Solution:
    def isPalindrome(self, s: str) -> bool:
        #initialise newStr convert to lowercase all letter
        #reverse newStr
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr[::-1] == newStr
        