class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # append day not yet found warmer temp to stack
        stack = []
        #initialise result array of 0
        result = [0] * len(temperatures)

        #iteate enumerate of input array
        for day, temperature in enumerate(temperatures):
            #while temp > temp of the elem on stack top we pop and update result  
            while(stack and temperature > temperatures[stack[-1]]):
                previous_day = stack.pop()
                result[previous_day] = day - previous_day
            #otherwise append to stack

            stack.append(day)
        return result