class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for number in nums1:
            index = nums2.index(number)
            next_greater = -1
            for i in range(index+1,len(nums2)):
                if nums2[i] > number:
                    next_greater = nums2[i]
                    break
            result.append(next_greater)
        return result
        