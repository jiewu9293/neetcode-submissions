class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for u,v,time_taken in times:
            graph[u].append((time_taken,v))
        infinity = float('inf')
        dist = [infinity for _ in range(n+1)]
        dist[k] = 0
        heap = [(0,k)]
        while heap:
            time_taken,node = heapq.heappop(heap)
            if time_taken > dist[node]:
                continue
            for travel_time,neighbor in graph[node]:
                new_time_taken = travel_time + time_taken
                if new_time_taken < dist[neighbor]:
                    dist[neighbor] = new_time_taken
                    heapq.heappush(heap,(new_time_taken,neighbor))
        last_arrival_time = max(dist[1:])
        if last_arrival_time == infinity:
            return -1 
        else:
            return last_arrival_time
    
