import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u,v,time_taken in times:
            graph[u].append((v, time_taken))
        infinity = float('inf')
        dist = [infinity] * (n+1)
        dist[k] = 0

        min_heap = [(k,0)]

        while min_heap:
            node,arrival_time = heapq.heappop(min_heap)
            if arrival_time > dist[node]:
                continue
            for neighbor,time_taken in graph[node]:
                new_time = arrival_time + time_taken
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(min_heap,(neighbor,new_time))
            
        last_time_taken = max(dist[1:])
        if last_time_taken == infinity:
            return -1 
        else:
            return last_time_taken
    
        

        
        