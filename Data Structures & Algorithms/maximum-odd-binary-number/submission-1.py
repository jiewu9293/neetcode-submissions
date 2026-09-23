class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Count the number of ones in the binary string.
        ones = s.count("1")
        #count num of zeros
        zeros = len(s) - ones
        #Reserve one '1' for the last position to make the number odd.
        # Put all other '1's at the front to maximize the binary value.
        return "1" * (ones-1) + "0"* zeros + "1"