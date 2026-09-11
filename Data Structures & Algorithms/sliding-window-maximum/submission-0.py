from collections import deque
#we need list to store max elem of each window
#we use queue to store index
#value of the index is monotonic decreasing
#elem not in the window remove its index from the queue
#remove index from queue such that its value can not be max in window
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        answer = []
        for i, num in enumerate(nums):
            if queue and queue[0] <= i - k:
                queue.popleft()
            
            while queue and nums[queue[-1]] <= num:
                queue.pop()

            queue.append(i)
            #when a window is formed
            #head of the queue is the index of the max elem in window
            if i >= k - 1:
                answer.append(nums[queue[0]])
        return answer
            