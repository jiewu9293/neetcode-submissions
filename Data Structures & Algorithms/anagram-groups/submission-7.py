class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap key:val key is each string the val is signature for each string
        res = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
            