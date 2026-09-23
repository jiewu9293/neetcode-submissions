class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Store the smallest and second smallest prices seen so far.
        first_min = float("inf")
        second_min = float("inf")
         # Store the smallest and second smallest prices seen so far.
        for price in prices:
            if price < first_min:
                second_min = first_min
                first_min = price
            elif price < second_min:
                second_min = price
        # Calculate the minimum cost of buying exactly two chocolates.
        minimum_cost = first_min + second_min
        if minimum_cost <= money:
            return money - minimum_cost
        return money


