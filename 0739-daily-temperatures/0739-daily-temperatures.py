class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n =len(temperatures)
        res = [0]*n
        stack = []
        for current_day, current_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < current_temp:
                prev_day = stack.pop()
                res[prev_day] = current_day - prev_day
            stack.append(current_day)
        return res        