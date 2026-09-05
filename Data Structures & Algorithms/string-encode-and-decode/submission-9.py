class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        #string = "hello"
        #5#hello len#
        for string in strs:
            parts.append(
                f"{len(string)}#{string}"
            )
        return "".join(parts)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            string_start = j + 1
            string_end = string_start + length 

            result.append(
            s[string_start:string_end]
            )

            i = string_end

        return result




