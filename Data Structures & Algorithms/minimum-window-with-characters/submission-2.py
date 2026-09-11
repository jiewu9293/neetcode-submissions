from collections import defaultdict,Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #substring as window
        #we need two pointer
        left = 0
        #expand the window as it moves to right
        #update the freq of the char added to window
        #moving right pointer to add the char to window
        #check if the char satisfy the freq in window
        #then check if window is valid, all char in window satisfy requirement 
        #we need to count freq in window
        #we also need to count freq in t and num of distinct in t
        #num of character satisfy the freq requirement in window

        #calculate current window length and compare with the best_length
        #if shorter than best_length update best_length
        #store the window
        #then reduce window try to find shorter window by moving left pointer
        #first we need to decrement the freq of the removed char in window
        #if the removed char satisfy freq requirement we decrement formed
        window = defaultdict(int)

        need = Counter(t)
        required = len(need)

        formed = 0
        best_length = float('inf')
        best_left = 0
        best_right = 0


        for right,char in enumerate(s):
            window[char] += 1

            if char in need and window[char] == need[char]:
                formed += 1

            while formed == required:
                current_length = right - left + 1
                if current_length < best_length:
                    best_length = current_length
                    best_left = left
                    best_right = right

                left_char = s[left]
                if left_char in need and window[left_char] == need[left_char]:
                    formed -= 1
                window[left_char] -= 1
                left += 1
        if best_length == float('inf'):
            return ''
        return s[best_left:best_right+1]

                

            
                        
        

