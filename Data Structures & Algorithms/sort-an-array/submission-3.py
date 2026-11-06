import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(left,right):
            if left >= right:
                return
             
            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]
            less = left
            current = left
            greater = right

            while current <= greater:
                if nums[current] < pivot:
                    nums[less], nums[current] = (
                        nums[current],
                        nums[less]
                    )
                    less += 1
                    current += 1

                elif nums[current] > pivot:
                    nums[greater], nums[current] = (
                        nums[current],
                        nums[greater]
                    )
                    greater -= 1
                
                else:
                    current += 1
            quick_sort(left, less - 1)
            quick_sort(greater + 1, right)
        quick_sort(0, len(nums) - 1)
        return nums
