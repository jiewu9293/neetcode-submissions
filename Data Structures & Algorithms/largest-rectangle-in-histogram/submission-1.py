class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = []
        #stack  (start_index,current_height)
        # iterate the input 
        # while when we see a shorter or equal bar we pop the stack
        # cal the area for the bar we just popped 
        # area = width * height
        # width = currentindex - previous_index
        # height = previous_height 
        # update the maxarea
        # update startindex for the current_height
        # current_height uses the previous index
        # else we see a taller bar we just append (current_index,current_hegith) to the stack
        # finally we cal area for the remaining bar on the stack
        # remaining bar can extend from its index and to the end of the input array width = len(heights)
        #return maxarea
        for current_index,current_height in enumerate(heights):
            start = current_index
            while stack and stack[-1][1] >= current_height:
                previous_index, previous_height = stack.pop()
                width = current_index - previous_index
                area = width * previous_height
                maxarea= max(maxarea,area)
                start = previous_index

            stack.append((start,current_height))
        for index, height in stack:
            maxarea = max(
                maxarea,
                (len(heights)-index) * height
            )
        return maxarea