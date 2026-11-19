class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        a XOR b gives the sum without carry.
        (a AND b) << 1 gives the carry.
        MASK keeps the result within 32 bits because Python integers do not have a fixed size.

        """
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        a &= MASK
        b &= MASK
        while b != 0:
            no_carry = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK 

            a = no_carry
            b = carry
        if a <= MAX_INT:
            return a
        return a-2**32