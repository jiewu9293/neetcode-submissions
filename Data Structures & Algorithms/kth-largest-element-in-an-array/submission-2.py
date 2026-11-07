import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        left = 0
        right = len(nums) - 1

        while left < right:
            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]

            smaller = left
            current = left
            greater = right

            while current <= greater:
                if nums[current] < pivot:
                    nums[smaller], nums[current] = (
                        nums[current],
                        nums[smaller],
                    )
                    smaller += 1
                    current += 1
                elif nums[current] > pivot:
                    nums[current], nums[greater] = (
                        nums[greater],
                        nums[current],
                    )
                    greater -= 1
                else:
                    current += 1 
                
            if target < smaller:
                right = smaller - 1
            elif target > greater:
                left = greater +1 
            else:
                return pivot 
        return nums[left]

                
            
                