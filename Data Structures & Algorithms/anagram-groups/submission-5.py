class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #count frequency each string have a dict, 26 keys value either 0 or 1
        # "cat" {0:1,1:0,2:1,3:,4:,5:..}
        res = defaultdict(list)
        for s in strs:
            count = [0] *26 #[0,0,...]
            for c in s:
                count[ord(c)-ord('a')] += 1 # "cat" count[2] += 1
            res[tuple(count)].append(s)
        return list(res.values())