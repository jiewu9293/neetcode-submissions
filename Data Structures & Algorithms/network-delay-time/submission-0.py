import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, travel_time in times:
            graph[u].append((v, travel_time))
        infinity = float('inf')
        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        heap = [(0, k)]
        while heap:
            arrival_time, node = heapq.heappop(heap)
            if arrival_time > dist[node]:
                continue
            for neighbor, travel_time in graph[node]:
                new_time = arrival_time + travel_time

                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(heap, (new_time, neighbor))
        max_arrival_time = max(dist[1:])
        if max_arrival_time == infinity:
            return -1
        else:
            return max_arrival_time


