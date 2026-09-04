class Solution:
    def isPalindrome(self, s: str) -> bool:
        #initialise 2 pointer r ,l 
        #"Was it a car or a cat I saw?"
        l,r = 0,len(s) - 1
        while r > l:
            while r > l and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    # determine if character is alphanum
    def alphaNum(self,c):
        return (ord('A') <= ord(c) <= ord('Z')
        or ord('a') <= ord(c) <= ord('z')
        or ord('0') <= ord(c) <= ord('9'))
