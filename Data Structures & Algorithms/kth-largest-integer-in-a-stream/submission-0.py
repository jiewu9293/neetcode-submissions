import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #maintain a heap with k elem
        self.k = k 
        self.heap = []
        #insert first k largest elem to heap
        for num in nums:
            heapq.heappush(self.heap,num)
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        #return root of the heap, is the minimum in the heap and the k largest 
        return self.heap[0]

        
