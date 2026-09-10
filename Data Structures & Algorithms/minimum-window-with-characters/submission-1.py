from collections import Counter,defaultdict
class Solution:
    #substring of s  as  a window
    #for the window to be valid
    #needs to contain all distinct characters in t
    #and freq of each char needs to be satisfied
    #we first expand the window until we find a valid substring
    #then we can reduce the window by moving left pointer to find a smaller substring
    #we need to store the best_window we find
    #after searching shortest valid window we can return the best window using python slicing
    #a window has left and right pointer
    
    def minWindow(self, s: str, t: str) -> str:
        #initialise a window
        left = 0
        #used to store the best window when we find better window we need to update these two variables
        best_left = 0
        best_right = 0
        # count 
        need = Counter(t)

        #count character freq in current window
        window = defaultdict(int)

        #count num of distinct characters we need in window
        required = len(need)

        #count number of distinct characters in window satisfy the frequency requirement
        formed = 0

        current_length = 0
        best_length = float("inf")
        for right,char in enumerate(s):
            #char added to window freq updated
            window[char] +=1 

            if char in need and window[char] == need[char]:
                formed += 1
            #all characters in window satisfy the requirement
            while formed == required:
                current_length = right -left + 1
                
                if current_length < best_length:
                    best_length = current_length
                    best_left = left
                    best_right = right
                #the substring is too big reduce window by moving left pointer
                left_char = s[left]
                #check char we going to remove
                if left_char in need and window[left_char] == need[left_char]:
                    #update formed 
                    formed -=1 
                #update window freq
                window[left_char] -= 1
                left += 1
        if best_length == float('inf'):
            return ""
        
        return s[best_left:best_right+1]

                
                
                
                


            






        
        