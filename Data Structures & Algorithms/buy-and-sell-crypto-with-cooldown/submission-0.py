class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        unreachable = float('-inf')
        n = len(prices)
        hold = [unreachable] * (n + 1)
        sold = [unreachable] * (n + 1)
        rest = [0] * (n + 1) 
        for day, price in enumerate(prices, start=1):
            hold[day] = max(hold[day-1],rest[day-1]-price)

            sold[day] = hold[day-1] + price
            rest[day] = max(sold[day-1],rest[day-1])

        return int(max(sold[n],rest[n]))