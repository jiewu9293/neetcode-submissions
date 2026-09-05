class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            first = nums[i]

            if first > 0:
                break
            if i >0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = first + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total >0:
                    right -= 1
                else:
                    result.append(
                        [first,nums[left],nums[right]]
                    )
                    left += 1
                    right -= 1
                    while(left<right and 
                nums[left] == nums[left-1]):
                        left += 1

                    while(left<right and nums[right] == nums[right+1]):
                        right -=1 
        return result

        