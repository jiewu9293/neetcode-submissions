class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n
        for current_day in range(n):
            while stack and temperatures[current_day] > temperatures[stack[-1]]:
                previous_day = stack.pop()
                result[previous_day] = current_day - previous_day
            stack.append(current_day)
        return result


        