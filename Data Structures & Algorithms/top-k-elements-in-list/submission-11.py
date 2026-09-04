class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build the freq table first
        # [cnt,num]
        #sort
        # take the top k.

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        arr = []
        for num,cnt in count.items():
            arr.append([cnt,num])

        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
            