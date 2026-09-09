class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                #target in left half and not equal to mid
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                #not in left half then target must be in right half
                else:
                    left = mid + 1 
            #right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 
                else:
                    right = mid -1 
        
        return -1
