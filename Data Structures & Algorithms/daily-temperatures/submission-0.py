class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialise to 0 
        result = [0] * len(temperatures)
        #stack store the day which not yet found warmer temp
        stack = []

        for day, temperature in enumerate(temperatures):
            while(stack and 
            # > not  >= use while not if 
            temperature > temperatures[stack[-1]]):

                previous_day =stack.pop()
                result[previous_day] = day - previous_day
            #append day to stack 
            stack.append(day)
        return result

        