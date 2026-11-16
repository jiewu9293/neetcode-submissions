class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for u,v,time_taken in times:
            graph[u].append((time_taken,v))
        infinity = float('inf')
        best=[infinity for _ in range(n+1)]
        best[k] = 0
        heap = [(0,k)]

        while heap:
            min_time,node = heapq.heappop(heap)
            if min_time > best[node]:
                continue
            
            for edge,v in graph[node]:
                new_time = min_time + edge
                if new_time < best[v]:
                    best[v] = new_time
                    heapq.heappush(heap,(new_time,v))
        last_arrival = max(best[1:])
        if last_arrival == infinity:
            return -1 
        else:
            return last_arrival
        
            
