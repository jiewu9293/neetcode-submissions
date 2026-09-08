class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Treat the array like a linked list
        each index points to the next index given by its value.
        each index is a node   val tells the next node
        0 1 
        duplicate number (the entry point of the cycle).
        """
        slow = 0
        fast = 0
        # 第一阶段：找到环内相遇点
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # 第二阶段：找到环的入口
        finder = 0
        while slow != finder:
            finder = nums[finder]
            slow = nums[slow]
        return finder
            