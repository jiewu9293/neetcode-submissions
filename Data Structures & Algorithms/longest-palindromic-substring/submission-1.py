class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right  += 1
            return left + 1, right
        
        best_start, best_end = 0, 1

        for i in range(len(s)):
            for left, right in ((i, i), (i, i + 1)):
                start , end = expand(left,right)

                if end - start > best_end - best_start:
                    best_start,best_end = start, end
        return s[best_start:best_end]