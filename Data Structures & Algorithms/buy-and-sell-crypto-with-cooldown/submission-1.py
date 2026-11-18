class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        unreachable = float('-inf')
        n = len(prices)
        sold = [unreachable] * (n+1)
        hold = [unreachable] * (n+1)
        rest = [0] * (n+1)

        for day,price in enumerate(prices,start=1):
            sold[day] = hold[day-1] + price

            hold[day] = max(rest[day-1] - price,hold[day-1])

            rest[day] = max(rest[day-1],sold[day-1])

        return int(max(sold[n],rest[n]))
