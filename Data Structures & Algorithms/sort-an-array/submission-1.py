class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n  = len(nums)
        temp = [0] * n
        def merge_sort(left,right):
            if left >= right:
                return 

            mid = left + (right - left) //2 

            merge_sort(left,mid)
            merge_sort(mid+1,right)

            i = left 
            j = mid + 1
            k = left
            while i <= mid and j <= right:
                if nums[i] < nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]   
                    j += 1
                k +=1 
            while i <= mid:
                temp[k] = nums[i]
                k+=1 
                i+= 1
            while j <=right:
                temp[k] = nums[j]
                k+=1 
                j+=1 
            for index in range(left,right+1):
                nums[index] = temp[index]
        merge_sort(0,n-1)
        return nums
                
