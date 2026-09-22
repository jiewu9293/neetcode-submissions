import heapq    
class MedianFinder:

    def __init__(self):
        #heap for smaller half
        self.small = []
        #heap for larger half
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        largest_in_small = -heapq.heappop(self.small)
        heapq.heappush(self.large, largest_in_small)
        # Step 3: Keep small the same size as large,
        # or one element larger than large
        if len(self.large) > len(self.small):
            smallest_in_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -smallest_in_large)

    def findMedian(self) -> float:
        # Odd number of elements: small has one extra element.
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        # Even number of elements: average the two middle values.
        return (-self.small[0] + self.large[0]) / 2.0

        
        
        