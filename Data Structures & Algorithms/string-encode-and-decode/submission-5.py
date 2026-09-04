class Solution:

    def encode(self, strs: List[str]) -> str:
        #["Hello","World"] “5,5,#HelloWorld"
        if not strs:
            return ""
        sizes,res = [],""
        for s in strs:
            #[5,5]
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res += ','
        #"5,5,"
        res += "#"
        #"5,5,#"
        for s in strs:
            res += s
        # "5,5,#HelloWorld"
        return res


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [],[],0
        while s[i] != '#':
            cur = ""
            #"4,4,#neetcode"
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        # [4,4]
        for sz in sizes:
            res.append(s[i:i+sz])
            i += sz
        return res

            
        