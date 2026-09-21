import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        do not need to calculate the square root because it does not change the relative ordering of the distances.
        """
        max_heap = []
        for x, y in points:
            # Squared distance is enough for comparison.
            distance = x * x + y * y

            # Add the current point to the heap.
            heapq.heappush(max_heap, (-distance, x, y))

            # # Keep only the k closest points.
            # If the heap contains more than k points,
            # remove the point with the largest real distance.
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [[x,y] for _,x,y in max_heap]