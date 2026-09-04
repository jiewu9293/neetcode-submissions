class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort
        #count table
        #fixed i ,j 
        #calculate 3rd target
        #check target exist?
        #[-1,0,1,2,-1,-4]
        # {-1:2,0:1,1:1,2:1,-4:1}
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1,len(nums)):
                count[nums[j]] -= 1
                if j> i+1 and nums[j] == nums[j-1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i],nums[j],target])
            for j in range(i+1, len(nums)):
                count[nums[j]] += 1 
        return res


