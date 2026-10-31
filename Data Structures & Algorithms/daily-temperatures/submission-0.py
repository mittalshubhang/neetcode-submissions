class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days = len(temperatures)
        res = [0]*(days)

        if days == 1:
            return [0]

        for i in range(days):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                lowerTempDay = stack.pop()
                res[lowerTempDay] = i-lowerTempDay
            stack.append(i)

        return res
            


        