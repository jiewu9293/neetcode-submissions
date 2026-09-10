class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        if window_size > len(s2):
            return False

        target = [0] * 26
        window = [0] * 26
        #count freq in window and s1
        for i in range(window_size):
            target[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        #check if window is permutation of s1 
        if target == window:
            return True
        # move fixed length window to right
        for right in range(window_size, len(s2)):
            #new char added to window and count freq
            window[ord(s2[right]) - ord('a')] += 1
            #old char removed from window and update freq_count

            left = right - window_size
            window[ord(s2[left]) - ord('a')] -= 1

            if target == window:
                return True
        return False
            
