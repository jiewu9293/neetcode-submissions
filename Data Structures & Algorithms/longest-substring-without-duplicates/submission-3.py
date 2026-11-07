class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_length = 0
        for right, character in enumerate(s):
            if character in last_seen and last_seen[character] >= left:
                left = last_seen[character] + 1
            
            last_seen[character] = right
            current_length = right - left + 1

            max_length = max(max_length,current_length)
        return max_length

