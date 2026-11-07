import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        left = 0
        right = len(nums) - 1 
        while left < right:
            pivot_index = random.randint(left,right)
            pivot = nums[pivot_index]

            less = left 
            greater = right
            current = left
            while current <= greater:
                if nums[current] < pivot:
                    nums[less],nums[current] = (nums[current],nums[less])
                    
                    less+= 1
                    current += 1
                elif nums[current] > pivot:
                    nums[greater],nums[current] = (nums[current],nums[greater])
                    
                    greater -= 1
                else:
                    current +=1 
            if target < less:
                right = less - 1
            elif target > greater:
                left = greater + 1
            else:
                return pivot 
        return nums[left]
        

                