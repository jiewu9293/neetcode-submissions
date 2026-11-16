class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for (u,v),prob in zip(edges,succProb):
            graph[u].append((prob,v))
            graph[v].append((prob,u))
        
        best = [0 for _ in range(n)]
        best[start_node] = 1
        heap = [(-1,start_node)]
        while heap:
            neg_prob,node = heapq.heappop(heap)
            prob = -neg_prob
            if prob < best[node]:
                continue
            if node == end_node:
                return prob
            for edge,v in graph[node]:
                new_prob = prob * edge
                if new_prob > best[v]:
                    best[v] = new_prob
                    heapq.heappush(heap,(-new_prob,v))
        return best[end_node]
            


            
            