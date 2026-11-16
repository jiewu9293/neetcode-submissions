import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        dist = [0.0] * n
        dist[start_node] = 1.0

        heap = [(-1.0, start_node)]
        while heap: 
            neg_prob, u = heapq.heappop(heap)
            prob = -neg_prob
            if prob < dist[u]:
                continue
            for v, edge_prob in graph[u]:
                new_prob = prob * edge_prob
                if new_prob > dist[v]:
                    dist[v] = new_prob
                    heapq.heappush(heap,(-new_prob,v))
        return dist[end_node]