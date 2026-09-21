import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        #transform list to heap so the root of the heap is the min value
        heapq.heapify(max_heap)

        # Continue until at most one stone remains.
        while len(max_heap) > 1:
            # Remove the two heaviest stones.
            heaviest = -heapq.heappop(max_heap)
            second_heaviest = -heapq.heappop(max_heap)
             # If their weights are different, push the difference back.
            if heaviest != second_heaviest:
                remaining_weight = heaviest - second_heaviest
                heapq.heappush(max_heap, -remaining_weight)
        # Return the last stone's weight, or 0 if no stone remains.
        return -max_heap[0] if max_heap else 0
                