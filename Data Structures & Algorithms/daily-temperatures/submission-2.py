class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for current_day in range(n):
            current_temperature = temperatures[current_day]
            while (
                stack
                and current_temperature > temperatures[stack[-1]]
            ):
                previous_day = stack.pop()
                answer[previous_day] = current_day - previous_day

            stack.append(current_day)

        return answer





