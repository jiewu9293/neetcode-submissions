class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, number in enumerate(nums):
            needed = target - number
            if needed in seen:
                return [seen[needed],index]
            seen[number] = index
        
