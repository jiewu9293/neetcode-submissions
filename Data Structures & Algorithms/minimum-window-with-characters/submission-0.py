from collections import Counter, defaultdict
"""
return length of shortest substring in s 
such substring contains every char in t
not exist return ""
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        #count freq for each char in t
        #character freq required in window
        need = Counter(t)
        # count char freq in window
        window = defaultdict(int)
        left = 0

        #number of distinct char in t 
        required = len(need)
        # number of char meet the freq required
        formed = 0

        best_length = float("inf")
        #when we find a valid window if its length shorter we need to udpate best_left best_right to do so
        best_left = 0
        best_right = 0

        for right, char in enumerate(s):
            #move right to expand window
            window[char] += 1
            #if the char in need and meet the required fred
            if char in need and window[char] == need[char]:
                formed += 1
            #when all distinct characters required are in window
            while formed == required:
                current_length = right - left + 1 
            #check if window is shorter  
                if current_length < best_length:
                    best_length = current_length
                    best_left = left
                    best_right = right
                #try to reduce window to find shorter valid substring
                left_char = s[left]
                if left_char in need and window[left_char] == need[left_char]:
                    formed  -= 1
                window[left_char] -= 1
                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_left:best_right+1] 

                 
                

            
