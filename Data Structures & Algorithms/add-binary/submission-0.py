class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []

        i = len(a) -1 
        j = len(b) -1 
        while i >= 0 or j >= 0 or carry:
            digita = int(a[i]) if i >= 0 else 0
            digitb = int(b[j]) if j >= 0 else 0

            total = digita + digitb + carry

            result.append(str(total % 2))

            carry = total // 2

            i -= 1
            j -=1 
        return "".join(reversed(result))