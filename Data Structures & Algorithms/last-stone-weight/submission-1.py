import heapq
#transform minheap to maxheap
#pop the heap 2 times
#until at most only one stoneweight in heap
#if 2 weights differ
#find the difference
#push difference to heap
#return the final weight  else return 0 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-weight for weight in stones]
        #list to maxheap
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            heaviest = -heapq.heappop(max_heap)
            second_heaviest = -heapq.heappop(max_heap)

            if heaviest != second_heaviest:
                difference = heaviest - second_heaviest
                heapq.heappush(max_heap,-difference)
        return -max_heap[0] if max_heap else 0 
            

        