class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        in_tree = [False] * n
        min_cost = [float('inf') for _ in range(n)]
        min_cost[0] = 0
        total_cost = 0
        for _ in range(n):
            next_point = -1 
            for i in range(n):
                if not in_tree[i] and (next_point==-1 or min_cost[i] < min_cost[next_point]):
                    next_point = i
            in_tree[next_point] = True
            total_cost += min_cost[next_point]
            x, y = points[next_point]
            

            for i,(other_x,other_y) in enumerate(points):
                if not in_tree[i]:
                    distance = abs(x-other_x) + abs(y-other_y)
                    if distance < min_cost[i]:
                        min_cost[i] = distance
        return total_cost
                