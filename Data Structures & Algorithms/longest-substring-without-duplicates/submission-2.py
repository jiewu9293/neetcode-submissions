class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        l = left edge of the window
r = right edge that moves through the string
last_seen store the index
        """
        left = 0
        last_seen = {}
        max_length = 0
        for right, char in enumerate(s):
            if char in last_seen:
                left = max(left, last_seen[char] + 1)
            last_seen[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length