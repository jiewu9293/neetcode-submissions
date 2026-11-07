class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        need = Counter(t)

        window = {}
        required = len(need)

        formed = 0
        left = 0

        best_left = 0
        best_length = float("inf")
        for right, char in enumerate(s):
            if char in need:
                window[char] = window.get(char, 0) + 1

                if window[char] == need[char]:
                    formed += 1
                while formed == required:
                    current_length = right - left + 1

                    if current_length < best_length:
                        best_left = left
                        best_length = current_length


                    left_char = s[left]
                    if left_char in need:
                        if window[left_char] == need[left_char]:
                            formed -= 1
                        window[left_char] -= 1
                    left += 1
        if best_length == float("inf"):
            return ""
        return s[best_left:best_left+best_length]
                                        



