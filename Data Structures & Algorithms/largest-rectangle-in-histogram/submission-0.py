class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack (start_index,height)
        """
        For each bar, we want to know how far it can stretch left and right
        heights = [5, 6, 2]
        area = height * width
        [(startindex,height)] earliest index where that height can start
        a new bar that is shorter than the top of the stack, it means the taller bar on top can’t extend further to the right.
        then calculate the area for the taller bar on top stack and update maxarea
        
        Each bar is pushed and popped at most once
        width = current_index - start_index
        """
        stack = []
        max_area = 0
        for index, current_height in enumerate(heights):
            start = index
            while(stack and stack[-1][1] >= current_height):
                previous_start, previous_height = stack.pop()

                width = index - previous_start
                area = previous_height * width
                #update startindex for the current height
                start = previous_start
                max_area = max(max_area, area)

                start = previous_start
            stack.append((start, current_height))
        #cal the area for the remain bar on the stack
        # the remaining bar can extend from the start to the end of the array   width = len(heights)
        for start, height in stack:
            max_area = max(
                max_area,
                height * (len(heights) - start),
            )
        return max_area

